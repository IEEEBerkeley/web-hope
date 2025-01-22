---
layout: page
title: Staff
nav_exclude: false
description: A listing of all the course staff members.
---

# Staff

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Teaching Assistants

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

## Office Hours

Staff will try their best to remove themselves from the calendar at least 24 hours prior to the start of their office hours. If you see a staff member on the calendar, feel free to drop in and ask them questions!

<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FLos_Angeles&mode=WEEK&showPrint=0&src=Y19zNHVpbDdwa2d0NXZnYTRtNzAwYTVuaWRuNEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F4511E" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>