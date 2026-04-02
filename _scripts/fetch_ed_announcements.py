import os
import re
import requests
from datetime import datetime
from pathlib import Path

ED_API_BASE = "https://us.edstem.org/api"
COURSE_ID = os.environ.get("ED_COURSE_ID", "95724")
ED_TOKEN = os.environ["ED_API_TOKEN"]

ANNOUNCEMENTS_DIR = Path(__file__).resolve().parent.parent / "_announcements"

STAFF_ROLES = {"admin", "staff", "teacher", "tutor", "ta"}


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


def is_staff_post(thread):
    user = thread.get("user", {})
    course_role = (user.get("course_role") or "").lower()
    role = (user.get("role") or "").lower()
    return course_role in STAFF_ROLES or role in STAFF_ROLES


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def main():
    ANNOUNCEMENTS_DIR.mkdir(exist_ok=True)
    threads = fetch_threads()

    staff_posts = [t for t in threads if is_staff_post(t)]
    print(f"Found {len(staff_posts)} staff posts out of {len(threads)} total threads.")

    existing = {f.stem for f in ANNOUNCEMENTS_DIR.glob("*.md")}
    new_count = 0

    for post in staff_posts:
        title = post.get("title", "Untitled")
        created_at = post.get("created_at", "")
        document = post.get("document", "")
        content = post.get("content", "")
        user = post.get("user", {})
        author = user.get("name", "Staff")
        category = post.get("category", "")
        thread_type = post.get("type", "post")

        body = document if document else content

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

        front_matter = f"""---
title: "{title.replace('"', '\\"')}"
date: {date_str}
author: "{author.replace('"', '\\"')}"
category: "{category}"
type: "{thread_type}"
---

{body}
"""
        filepath = ANNOUNCEMENTS_DIR / f"{slug}.md"
        filepath.write_text(front_matter, encoding="utf-8")
        print(f"Created: {filepath.name}")
        new_count += 1

    print(f"Done. {new_count} new post(s) added, {len(staff_posts)} staff posts total.")


if __name__ == "__main__":
    main()
