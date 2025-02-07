---
layout: page
title: GitHub Desktop
nav_exclude: true
description: GitHub Desktop installation and crash course
permalink: /github_desktop
---

GitHub Desktop  
==============

* Do not remove this line (it will not be displayed)
{:toc}

Git is a version control system that allows multiple people to work on the same project without overwriting each other's changes.

There are a number of different Git services out there, but GitHub is by far the most popular.  It is free even for private repositories, and has a number of features that make it easy to use.

Typically Git is used through a command line

# Installation
## Windows
### Official Installer
Download and run the GitHub Desktop installer from the official website: [https://desktop.github.com/download/](https://desktop.github.com/download/)

### WinGet
From an administrator-level command prompt, run
`winget install GitHub.GitHubDesktop`

## MacOS
### Official Installer
Download and run the GitHub Desktop installer from the official website: [https://desktop.github.com/download/](https://desktop.github.com/download/)

### Homebrew

Run the command found here: [https://formulae.brew.sh/cask/github](https://formulae.brew.sh/cask/github)

# Basic Usage
## Creating and Sharing a Repository
> Only one person on your team needs to create the repository!  Anyone who does not do this should skip to the next section.
+ Go to [https://github.com/new](https://github.com/new) to create a new repository.
<img src="/assets/note6/github-new.png" style="border-radius: 1em" alt="GitHub repository creation page">
+ Enter a name for your repository, and an optional description
+ Choose to keep your repository Public or Private.  We suggest keeping it private, at least for now.
+ Select the `KiCad` option for the `.gitignore` template.
+ Click `Create repository`

Now that you've created your repository, you'll need to share it with your teammates!

## Cloning a Repository
