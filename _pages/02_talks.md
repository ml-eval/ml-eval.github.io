---
layout: page
title: Talks
permalink: /talks/
description: We have invited the following speakers:
nav: true
horizontal: false
---


{% for speaker in site.speakers %}
<h1 id="{{ speaker.anchor }}"><a href="{{ speaker.website }}">{{ speaker.name }}</a></h1>
<table style="width:100%">
  <tr>
    <td>
    <img class="thumbnail" src="../{{ speaker.img_path }}" alt="">
    </td>
    <td style="text-align:left">TBD</td>
  </tr>
</table>
{%- endfor %}
