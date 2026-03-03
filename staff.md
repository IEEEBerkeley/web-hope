---
layout: page
title: Staff
nav_exclude: false
description: A listing of all the course staff members.
---

# Staff

## Hope Directors

<div style="
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(345px, 1fr));
    width: 100%
">
    {% assign directors = site.staffers | where: 'name', 'Curtis Suero Manacsa' %}
    {% for staffer in directors %}
    {{ staffer }}
    {% endfor %}
    {% assign directors = site.staffers | where: 'name', 'Roman Silivra' %}
    {% for staffer in directors %}
    {{ staffer }}
    {% endfor %}
    
</div>

## Staff

<div style="
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(345px, 1fr));
    width: 100%
">
    {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
    {% for staffer in instructors %}
        {% unless staffer.name == 'Curtis Suero Manacsa' or staffer.name == 'Roman Silivra' %}
        {{ staffer }}
        {% endunless %}
    {% endfor %}
    
</div>

# Legacy Staffers

<div style="
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(345px, 1fr));
    width: 100%
">
    {% for staffer in site.legacy_staffers %}
    {{ staffer }}
    {% endfor %}
    
</div>

## Office Hours

Staff will try their best to remove themselves from the calendar at least 24 hours prior to the start of their office hours. If you see a staff member on the calendar, feel free to drop in and ask them questions!

<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FLos_Angeles&mode=WEEK&showPrint=0&src=Y19zNHVpbDdwa2d0NXZnYTRtNzAwYTVuaWRuNEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F4511E" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>