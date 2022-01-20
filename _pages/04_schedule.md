---
layout: page
title: Schedule
permalink: /schedule/
description: Tentative schedule. This will likely change significantly.
nav: true
horizontal: true
---

<table style="width:75%">
        <tr>
        <th style="text-align:right">Time (UTC)</th>
        <th style="text-align:left">Session</th>
        </tr>
    {% for time in site.data.schedule %}
        <tr>
        <td style="text-align:right">{{ time.start }} - {{ time.end }} </td>
        <td style="text-align:left">{{ time.description }}</td>
        </tr>
    {% endfor %}
</table>
