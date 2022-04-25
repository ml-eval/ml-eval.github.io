---
layout: page
title: Papers
permalink: /accepted-papers/
description:
nav: true
horizontal: false
---


{% assign sections = "Orals|Posters" | split: "|" %}
{%- for section in sections %}
  <h2>{{ section }}</h2>
  {%- for paper in site.papers %}

  {%- if section == 'Orals' and paper.oral == "true" %}
<div class='paper'>
  <h4 class='pdf' id="{{ paper.id}}">
    <!-- <div class='pdf'>[<a href='../assets/pdf/{{ paper.pdf }}'>PDF</a>]</div> -->
    <!-- <div class='video'>[<a href='{{ paper.video }}'>Video</a>]</div> -->
    {{ paper.title}}
    <a href='/accepted-papers#{{ paper.id}}'><div class="anchor"></div></a>
  </h4>
  <h5 style='font-style: italic;'>
    {{ paper.authors }}
  </h5>
  <span>[<a href='../assets/pdf/{{ paper.pdf }}'>PDF</a>]</span>
  {% if paper.video != '' %}
    <span>[<a href='{{ paper.video }}'>Video</a>]</span>
  {% endif %}
  {% if paper.poster != '' %}
    <span>[<a href='{{ paper.poster}}'>Poster</a>]</span>
  {% endif %}
  <p>
    {{ paper.abstract }}
  </p>
</div>
  {%- elsif section == 'Posters' and paper.oral == "false" %}
<div class='paper'>
  <h4 class='pdf' id="{{ paper.id}}">
    <!-- <div class='pdf'>[<a href='../assets/pdf/{{ paper.pdf }}'>PDF</a>]</div> -->
    <!-- <div class='video'>[<a href='{{ paper.video }}'>Video</a>]</div> -->
    {{ paper.title}}
    <a href='/accepted-papers#{{ paper.id}}'><div class="anchor"></div></a>
  </h4>
  <h5 style='font-style: italic;'>
    {{ paper.authors }}
  </h5>
  <span>[<a href='../assets/pdf/{{ paper.pdf }}'>PDF</a>]</span>
  {% if paper.video != '' %}
    <span>[<a href='{{ paper.video }}'>Video</a>]</span>
  {% endif %}
  {% if paper.poster != '' %}
    <span>[<a href='{{ paper.poster}}'>Poster</a>]</span>
  {% endif %}

  <p>
    {{ paper.abstract }}
  </p>
</div>
  {%- endif -%}

  {%- endfor %}
{%- endfor %}
