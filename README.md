# Pathogenseq lab website

This repo hosts the pathogenseq lab website.
The website uses github's built in jekyll static site generator to create a website at [https://lshtmpathogenseqlab.github.io/](https://genomics.lshtm.ac.uk/) using markdown files.

## Modifying

It is fairly straightforward to add pages. At the moment you can add yourself in the people page, add projects in the project page and new research themes.

### People

If you want to add yourself to the "People" page then create a markdown file in `/collections/_people/` using the first character of your forname and your full surname. E.g. Jody Phelan -> `/collections/_people/jphelan.md`. Use the follwing template:

```
--- 
layout: people
alumni: false
pid: jthorpe
forname: Joseph
surname: Thorpe 
title: Research fellow 
Important-fact: Passionate chess player and Roman history geek 
tags:   
- Malaria
- Bioinformatics   
- Drug-resistance 

---

Initially graduated in Biomedicine from Nottingham Trent university, I decided to take a different direction and graduated with an MSc in Bioinformatics from Cranfield University. From there I learned how to visualise genomic data via fancy websites and create Java applications.

```
The top section demarked by "---" are variables which the system needs to populate your page:
 - layout - keep this as "people"
 - pid - use the same naming scheme as the filename
 - tags - add any keywords you would like to be associated with yourself

Any other text is rendered at the top of your personalised page. You can use this to write about what you do.

If you would like a picture of yourself to be added then put a jpg file in `/assets/img/` using the pid as the name (e.g. `/assets/img/jphelan.jpg`).

### Projects

If you want to add new projects, you can do so by adding a markdown file to the `/collections/_projects/` folder using the following template.

```
---
layout: default
name: TB-Profiler
theme: tuberculosis
people:
  - gnapier
  - jphelan
---

This project page describes TB-Profiler
```

Again, there are some variables at the top of the page which need to be defined. 
 - name - the project name
 - theme - which research theme it belongs to (e.g. tuberculosis, malaria). If your theme isn't created yet, look at the next section
 - people - add anyone who is associated with the project

### Themes

Projects are arranged under research themes. You can add you theme by adding a markdown file to `/collections/_themes/` using the following template.

```
---
layout: theme
name: tuberculosis
---

All tuberculosis projects will be listed here

```
