---
layout: page
title: Schedule
permalink: /schedule/
description: Official schedule.
nav: true
horizontal: true
---

## The workshop will take place on April 29th during ICLR 2022.

<table style="width:100%">
        <tr>
        <th style="text-align:right">Time (UTC)</th>
        <th style="text-align:left">Session</th>
        </tr>
    {% for time in site.data.schedule %}
        <tr>
        <td style="text-align:right">{{ time.start }} - {{ time.end }} </td>
        <td style="text-align:left"><strong>{{ time.categories}}</strong> {{ time.title }}<br/>{{ time.desc}}</td>
        </tr>
    {% endfor %}
</table>
