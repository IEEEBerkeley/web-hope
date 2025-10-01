---
layout: page
title: GitHub Desktop
nav_exclude: true
description: GitHub Desktop installation and crash course
permalink: /github-desktop
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
- Free hosting for both public and private projects

While Git traditionally requires command-line expertise (see the [Git Handbook](https://docs.github.com/en/get-started/using-git/about-git) for the basics), GitHub Desktop provides a visual interface that makes version control more accessible to beginners.  



# Installation
Choose any one of these installation options corresponding to your operating system!
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
## Creating and Sharing a Repository with Github Classroom
+ Follow this link to accept the assignment: [https://classroom.github.com/a/wL2dZu3n](https://classroom.github.com/a/wL2dZu3n) *(Fall 2025)*
+ Create or join your team
+ Accept the assignment to create your repository
+ You may have to accept the assignment through an email!

<!-- > Only one person on your team needs to create the repository!  Anyone who does not do this should skip to the next section. -->
<!-- + Go to [https://github.com/new](https://github.com/new) to create a new repository.
<img src="/assets/note6/github-new.png" style="border-radius: 1em" alt="GitHub repository creation page">
+ Enter a name for your repository, and an optional description
+ Choose to keep your repository Public or Private.  We suggest keeping it private, at least for now.
+ Select the `KiCad` option for the `.gitignore` template.
+ Click `Create repository`

Now that you've created your repository, you'll need to share it with your teammates!

+ Go to your new repository's collaborator page on Github (e.g. https://github.com/{username}/{repository}/settings/access)

+ Add your teammates as collaborators by clicking the "Add People" button and entering their GitHub usernames or email addresses.

+ In the future, it may be helpful to share your repository with your project mentors as well, so they can provide feedback and help troubleshoot any issues.

<img src="/assets/note6/github-sharing.png" style="border-radius: 1em" alt="GitHub repository collaborators page"> -->

## Cloning a Repository

+ Sign into your GitHub account in GitHub Desktop
+ Press `Ctrl + Shift + O` or click `File > Clone Repository` to open the Clone Repository dialog
+ Select your project repository from the list of your repositories on GitHub (it will show up under the IEEE-HOPE Github organization)
+ Choose a local path to clone the repository to
+ Click `Clone`

## Making Changes, Committing, and Pushing
Before you start making changes to your project, you should pull the latest changes from the repository to make sure you are working with the most up-to-date version of the project.

+ Open GitHub Desktop
+ Open your repository (if it is not already open)
+ Click `Repository > Pull` to pull the latest changes from the repository

{: .warning}
> If you make changes to your project before pulling the latest changes, you would be doing work on an outdated version of the project.  This can lead to conflicts when you try to push your changes back to the repository.  Always pull the latest changes before you start working on your project, and talk to your teammates if you encounter conflicts!

Every time you make changes and want to save them to the repository, you need to commit them.  This is like saving a snapshot of your project at a particular point in time.

+ Open GitHub Desktop
+ Open your repository (if it is not already open)
    + You will see a list of changes you have made since the last commit
+ Enter a "commit message" of the changes you made in the `Summary` field
    + You can also enter a more detailed description in the `Description` field
    > It is good practice to write a descriptive commit message that explains what you changed and why, so it's easy to find later if you need to revert or understand why a change was made!
+ Click `Commit to main` to save your changes to the repository
+ Click `Push origin` to send your changes to the repository on GitHub

## File Structure
This is by no means necessary, but we suggest you follow a file structure similar to the one below to keep your project organized:

```
project/
├── project.kicad_pro
├── project.kicad_pcb
├── project.kicad_sch
libraries/
├── project_symbol_library.kicad_sym
├── project_footprint_library.pretty/
```

# Video Tutorial

If you prefer to learn by watching, here is a good video tutorial that covers the basics of using Git for KiCad version control:

<iframe width="896" height="504" src="https://www.youtube.com/embed/YCKeqBlQyJQ?si=SI-hVz0a9HZNLg6y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# PDM with KiCad
We have not personally used these tools, but they may be worth investigating for more advanced version control and project management needs:
- https://allspice.io/
- https://cadlab.io/