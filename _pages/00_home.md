---
layout: about
permalink: /
title: ICLR2022
description: TODO
nav: true
horizontal: false
---

TODO
# Call for papers

# Speakers

<table style="width:75%">
  <tr>
    {% for speaker in site.speakers limit:4 %}
        <td style="text-align:center"><img src="{{ speaker.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for speaker in site.speakers limit:4 %}
        <td style="text-align:center"><a href="{{ speaker.website }}"> {{ speaker.name }}</a> <br> {{ speaker.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for speaker in site.speakers offset:4 %}
        <td style="text-align:center"><img src="{{ speaker.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for speaker in site.speakers offset:4 %}
        <td style="text-align:center"><a href="{{ speaker.website }}"> {{ speaker.name }}</a> <br> {{ speaker.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>

# Panels

{%- for panel in site.panels %}

## {{ panel.name }}

**Moderator:** {{ panel.moderator }}

<table style="width:75%">
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><img src="{{ panelist.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><a href="{{ panelist.website }}"> {{ panelist.name }}</a> <br> {{ panelist.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for panelist in panel.panelists offset:3 %}
        <td style="text-align:center"><img src="{{ panelist.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for panelist in panel.panelists offset:3 %}
        <td style="text-align:center"><a href="{{ panelist.website }}"> {{ panelist.name }}</a> <br> {{ panelist.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>
{%- endfor %}

# Organizers

<table style="width:75%">
  <tr>
    {% for organizer in site.organizers limit:3 %}
        <td style="text-align:center"><img src="{{ organizer.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for organizer in site.organizers limit:3 %}
        <td style="text-align:center"><a href="{{ organizer.website }}"> {{ organizer.name }}</a> <br> {{ organizer.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for organizer in site.organizers offset:3 %}
        <td style="text-align:center"><img src="{{ organizer.img_path }}" alt="" height="175" width="175"></td>
    {% endfor %}
  </tr>
  <tr>
    {% for organizer in site.organizers offset:3 %}
        <td style="text-align:center"><a href="{{ organizer.website }}"> {{ organizer.name }}</a> <br> {{ organizer.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>


# Organizers affiliations
