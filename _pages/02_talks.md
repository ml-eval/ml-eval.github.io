---
layout: page
title: Talks
permalink: /talks/
description: Invited speakers:
nav: true
horizontal: false
---


{% for speaker in site.speakers %}
<table style="width:100%">
  <tr>
    <td style="width: 25%;">
      <h2><a href="{{ speaker.website }}">{{ speaker.name }}</a></h2>
    </td>
    <td> 
      <h2 id="{{ speaker.anchor }}">{{ speaker.title}}</h2>
    </td>
  </tr>
  <tr>
    <td colspan=2>
      {{speaker.abstract}}
    </td>
  </tr>
  <tr>
    <td >
      <img class="thumbnail" src="../{{ speaker.img_path }}" alt="">
    </td>
    <td style="text-align:left;">
      {{speaker.bio}}
    </td>
  </tr>

</table>
{%- endfor %}
