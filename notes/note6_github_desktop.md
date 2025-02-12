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

Git is a distributed version control system that revolutionizes how teams collaborate on software projects. It will:
- Tracks every modification to your code
- Maintains a complete history of who changed what and when
- Enables you to revert to previous versions if something goes wrong

It is typically used for software development, but can be applied to any project that requires version control.  PCB design (ECAD) and other CAD projects lose the advantage of merging individual files, but the ability to track changes, revert to previous versions, and quickly share files with collaborators is still invaluable.

GitHub is a web-based platform built around Git that adds:
- A user-friendly interface for managing Git repositories
- Tools for code review and project management
- The world's largest community of developers
- Free hosting for both public and private projects

While Git traditionally requires command-line expertise (see the [Git Handbook](https://docs.github.com/en/get-started/using-git/about-git) for the basics), GitHub Desktop provides a visual interface that makes version control more accessible to beginners.  



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
