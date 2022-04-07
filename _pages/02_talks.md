---
layout: page
title: Talks
permalink: /talks/
description: We have invited the following speakers
nav: true
horizontal: false
---


{% for speaker in site.speakers %}
<div style="width: 100%; display: table">
  <div style="display; table-row">
    <div style="width: 33%; display: table-cell; vertical-align: top;">
      <h2><a href="{{ speaker.website }}">{{ speaker.name }}</a></h2>
      <br/>
      <img class="thumbnail" src="../{{ speaker.img_path }}" alt="">
      <br/>
      <p style="font-size:.9rem;font-weight:300;line-height:1.2;">
      {{speaker.bio}}
      </p>
    </div>
    <div style="width: 65%; display: table-cell">
      <table style="width:100%">
        <tr>
          <td>
              <h2 id="{{ speaker.anchor }}">{{ speaker.title}}</h2>
          </td>
        </tr>
        <tr>
          <td style="text-align:left">{{speaker.abstract}}</td>
        </tr>
      </table>
    </div>
  </div>
</div>

<table style="width:100%">
  <tr>
    <td style="width: 75%;">
      <h2 id="{{ speaker.anchor }}">{{ speaker.title}}</h2>
    </td>
    <td style="width: 25%;">
            <h2><a href="{{ speaker.website }}">{{ speaker.name }}</a></h2>
    </td>
  </tr>
  <tr>
    <td style="text-align:left; width: 75%;"">
      <div style="width: 100%; display: table">
        <div style="display; table-row">
          <div style="width: 33%; display: table-cell; vertical-align: top;">
            <img class="thumbnail" src="../{{ speaker.img_path }}" alt="">
            <h2><a href="{{ speaker.website }}">{{ speaker.name }}</a></h2>
            <br/>
            <p style="font-size:.9rem;font-weight:300;line-height:1.2;">
            {{speaker.bio}}
            </p>
          </div>
          <div style="width: 65%; display: table-cell">
                {{speaker.abstract}}
          </div>
        </div> 
      </div>
    </td>
  </tr>
</table>

<table style="width:100%">
  <tr>
    <td style="width: 33%;">
      <h2><a href="{{ speaker.website }}">{{ speaker.name }}</a></h2>
    </td>
    <td> 
      <h2 id="{{ speaker.anchor }}">{{ speaker.title}}</h2>
    </td>
  </tr>
  <tr>
    <td style="text-align:left;">
      <img class="thumbnail" src="../{{ speaker.img_path }}" alt="">
      <p style="font-size:.9rem;font-weight:300;line-height:1.2;">
      {{speaker.bio}}
      </p>
    </td>
    <td>
      {{speaker.abstract}}
    </td>
  </tr>
</table>

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
