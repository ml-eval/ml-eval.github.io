---
layout: page
title: Panels
permalink: /panels/
description: TODO
nav: true
horizontal: false
---

{%- for panel in site.panels %}

<h1 id="{{ panel.anchor }}">{{ panel.name }}</h1>

**Moderator:** {{ panel.moderator }}

{{ panel.description }}

### Panelists

<table style="width:75%">
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><img class="thumbnail" src="../{{ panelist.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><a href="{{ panelist.website }}"> {{ panelist.name }}</a> <br> {{ panelist.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for panelist in panel.panelists offset:3 %}
        <td style="text-align:center"><img class="thumbnail" src="../{{ panelist.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for panelist in panel.panelists offset:3 %}
        <td style="text-align:center"><a href="{{ panelist.website }}"> {{ panelist.name }}</a> <br> {{ panelist.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>

{%- endfor %}
