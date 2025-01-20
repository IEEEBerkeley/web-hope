---
layout: page
title: KiCad Installation Guide
nav_exclude: true
description: KiCad Installation Guide
permalink: /labs/kicad_install
---

KiCad Installation Guide
==============

* Do not remove this line (it will not be displayed)
{:toc}

The KiCad installer is about 1.5 GB and install requires about 6GB of disk space.  Ask us for help if you run into any issues!

## Windows
### Official Installer *(Recommended)*
Download the KiCad 8.0 installer from the official website: [https://www.kicad.org/download](https://www.kicad.org/download/?ref=ieee.berkeley.edu)

Leave all installer options at their defaults.  You do not have to install FreeCAD at the end.

### WinGet
From an administrator-level command prompt, run
`winget install KiCad.KiCad`

## MacOS
### Official Installer *(Recommended)*
Download the KiCad 8.0 installer from the official website: [https://www.kicad.org/download](https://www.kicad.org/download/?ref=ieee.berkeley.edu)

Open the `.dmg` file, and drag the KiCad folder into Applications.  You may also want to save the demos folder somewhere, but this is not required.

### Homebrew
Run the command found here: [https://formulae.brew.sh/cask/kicad]

## Linux
**Note that instructor support is not guaranteed for Linux troubleshooting**

### Official Installer *(Recommended)*
Download the KiCad 8.0 installer from the official website: [https://www.kicad.org/download](https://www.kicad.org/download/?ref=ieee.berkeley.edu)

Installation process varies by distro.

### Package Manager
List of KiCad names by distro and corresponding package manager: [https://repology.org/project/kicad/versions]

# Running KiCad for the first time:
Open KiCad however you would typically open an app.  KiCad has this icon:

<img src="/assets/lab1/kicad_logo.png" style="width: 5em;border-radius: 1em" alt="KiCad Logo">

On the first startup, you will see a dialog box similar to this pop up.  Simply press OK to start with the default settings.

<img src="/assets/lab1/kicad_initial_config.png" style="border-radius: 0em" alt="KiCad initial configuration popup">

It may also pop up a data collection opt-in request, to which you can respond however you wish.

This should bring you to the project manager window.

<img src="/assets/lab1/kicad_project_manager.png" style="border-radius: 0em" alt="KiCad project manager home page">

At this point, you can simply exit KiCad.  Your KiCad installation is complete!