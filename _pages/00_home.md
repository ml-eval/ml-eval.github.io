---
layout: about
permalink: /
title: ICLR2022
description: TODO
nav: true
horizontal: false
---


The aim of the workshop is to discuss and propose standards for evaluating ML research,
in order to better identify promising new directions and to accelerate real progress in the field of
ML research. The problem requires understanding the kinds of practices that add or detract from the
generalizability or reliability of results reported, and incentives for researchers to follow best
practices. We may draw inspiration from adjacent scientific fields, from statistics, or history of
science. Acknowledging that there is no consensus on best practices for ML, the workshop will have a
focus on panel discussions and a few invited talks representing a variety of perspectives. The call
to papers will welcome opinion papers as well as more technical papers on evaluation of ML methods.
We plan to summarize the findings and topics that emerged during our workshop in a short report.
For any queries, please reach out to the organizers at <a href="mailto:ml-eval-iclr2022@googlegroups.com"> ml-eval-iclr2022@googlegroups.com </a>.

# [Call for papers](/call-for-papers)

We invite two types of papers -- opinion papers (up to 4 pages) stating positions on the topics
related to those listed above, and methodology papers (up to 8 pages excluding references) about
evaluation in ML. These topics may include: 

- Establishing benchmarking standards for ML research
- Reliable tools/protocols for benchmarking and evaluation
- Understanding and defining reproducibility for machine learning
- Meta analyses thoroughly evaluating existing claims across papers
- Incentives for doing better evaluation and reporting results

Submission Site: <a href="https://cmt3.research.microsoft.com/SMILES2022/"> https://cmt3.research.microsoft.com/SMILES2022 </a>


# [Speakers](/talks)

<table style="width:75%">
  <tr>
    {% for speaker in site.speakers limit:4 %}
        <td style="text-align:center"><img class="thumbnail" src="{{ speaker.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for speaker in site.speakers limit:4 %}
        <td style="text-align:center"><a href="/talks#{{ speaker.anchor}}"> {{ speaker.name }}</a> <br> {{ speaker.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for speaker in site.speakers offset:4 %}
        <td style="text-align:center"><img class="thumbnail" src="{{ speaker.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for speaker in site.speakers offset:4 %}
        <td style="text-align:center"><a href="/talks#{{ speaker.anchor}}"> {{ speaker.name }}</a> <br> {{ speaker.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>

# [Panels](/panels)

{%- for panel in site.panels %}

## [{{ panel.name }}](/panels#{{ panel.anchor }})

<table style="width:75%">
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><img class="thumbnail" src="{{ panelist.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for panelist in panel.panelists limit:3 %}
        <td style="text-align:center"><a href="{{ panelist.website }}"> {{ panelist.name }}</a> <br> {{ panelist.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for panelist in panel.panelists offset:3 %}
        <td style="text-align:center"><img class="thumbnail" src="{{ panelist.img_path }}" alt=""></td>
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
        <td style="text-align:center"><img class="thumbnail" src="{{ organizer.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for organizer in site.organizers limit:3 %}
        <td style="text-align:center"><a href="{{ organizer.website }}"> {{ organizer.name }}</a> <br> {{ organizer.affiliations }} </td>
    {% endfor %} 
  </tr>
  <tr>
    {% for organizer in site.organizers offset:3 %}
        <td style="text-align:center"><img class="thumbnail" src="{{ organizer.img_path }}" alt=""></td>
    {% endfor %}
  </tr>
  <tr>
    {% for organizer in site.organizers offset:3 %}
        <td style="text-align:center"><a href="{{ organizer.website }}"> {{ organizer.name }}</a> <br> {{ organizer.affiliations }} </td>
    {% endfor %} 
  </tr>
</table>


# Organizers affiliations
