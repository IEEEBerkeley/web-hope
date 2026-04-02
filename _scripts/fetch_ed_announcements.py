import os
import re
import json
import requests
from datetime import datetime
from pathlib import Path

ED_API_BASE = "https://us.edstem.org/api"
COURSE_ID = os.environ.get("ED_COURSE_ID", "95724")
ED_TOKEN = os.environ["ED_API_TOKEN"]

ANNOUNCEMENTS_DIR = Path(__file__).resolve().parent.parent / "_announcements"


def fetch_threads():
    headers = {"Authorization": f"Bearer {ED_TOKEN}"}
    threads = []
    offset = 0
    limit = 30

    while True:
        url = f"{ED_API_BASE}/courses/{COURSE_ID}/threads"
        print(f"Fetching: {url} (offset={offset})")
        resp = requests.get(
            url,
            headers=headers,
            params={"limit": limit, "offset": offset, "sort": "new"},
        )
        if not resp.ok:
            print(f"Error {resp.status_code}: {resp.text}")
        resp.raise_for_status()
        data = resp.json()
        batch = data.get("threads", [])
        if not batch:
            break
        threads.extend(batch)
        offset += limit
        if len(batch) < limit:
            break

    return threads


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def html_to_markdown(html):
    """Basic HTML to plain text conversion."""
    if not html:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<p>", "", text)
    text = re.sub(r"</p>", "\n\n", text)
    text = re.sub(r"<a\s+href=[\"']([^\"']+)[\"'][^>]*>([^<]+)</a>", r"[\2](\1)", text)
    text = re.sub(r"<strong>([^<]+)</strong>", r"**\1**", text)
    text = re.sub(r"<b>([^<]+)</b>", r"**\1**", text)
    text = re.sub(r"<em>([^<]+)</em>", r"*\1*", text)
    text = re.sub(r"<i>([^<]+)</i>", r"*\1*", text)
    text = re.sub(r"<li>([^<]*)</li>", r"- \1\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    ANNOUNCEMENTS_DIR.mkdir(exist_ok=True)
    threads = fetch_threads()

    announcements = [t for t in threads if t.get("type") == "announcement"]
    if not announcements:
        announcements = [t for t in threads if t.get("is_announcement")]
    if not announcements:
        print(f"No announcements found. Thread types: {set(t.get('type') for t in threads)}")
        print(f"Checking category field: {set(t.get('category') for t in threads)}")
        announcements = [t for t in threads if t.get("category", "").lower() == "announcements"]

    existing = {f.stem for f in ANNOUNCEMENTS_DIR.glob("*.md")}
    new_count = 0

    for ann in announcements:
        title = ann.get("title", "Untitled")
        created_at = ann.get("created_at", "")
        content = ann.get("content", ann.get("document", ""))

        if created_at:
            try:
                dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                date_str = dt.strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")

        slug = f"{date_str}-{slugify(title)}"
        if slug in existing:
            continue

        body = html_to_markdown(content) if "<" in str(content) else str(content or "")

        front_matter = f"""---
title: "{title.replace('"', '\\"')}"
date: {date_str}
---

{body}
"""
        filepath = ANNOUNCEMENTS_DIR / f"{slug}.md"
        filepath.write_text(front_matter, encoding="utf-8")
        print(f"Created: {filepath.name}")
        new_count += 1

    print(f"Done. {new_count} new announcement(s) added, {len(announcements)} total found.")


if __name__ == "__main__":
    main()
