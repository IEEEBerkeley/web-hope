---
layout: fullwidth
title: Hands-On PCB Engineering (HOPE)
nav_exclude: true
permalink: /:path/
seo:
  type: Course
  name: Berkeley IEEE HOPE
---

# Hands-On PCB Engineering (HOPE) [Spring 2026]
<!-- {:.no_toc} -->

{%- if site.under_construction -%}
<p class="warning">
This site is under construction. All dates and policies are tentative until this message goes away.
</p>
{%- endif -%}

{%- if site.waitlist_warning -%}
<p class="warning">
If you're currently on the waitlist, or have any other course-related logistics questions, please take a look at our <a href="{{ site.baseurl }}/policies/">Course Policies</a> prior to contacting course staff.
</p>
{%- endif -%}

{%- if site.outdated -%}
<p class="warning">
This website contains materials from a past semester. Information, assignments, and announcements may no longer be relevant. Please refer to the <a href="https://template.cs161.org">current semester's site</a> for up-to-date content.
</p>
{%- endif -%}

**Lecture:** 8-10PM WeTh, Cory 125

<!-- _[Attendance Form](http://berkie.ee/hope-sp25-attendance)    [Lab Checkoff Form](http://berkie.ee/hope-sp25-checkoff)_ -->

<table id="timeline" style="line-height: normal;">
    <tbody><tr>
      <th style="width: 5%;">Week</th>
      <th style="width: 35%;">Topic</th> 
      <th style="width: 15%;">Reference</th>
      <th style="width: 15%;">Lab</th>
      <th style="width: 15%;">Lab Checkoff Due</th>
      <th style="width: 15%;">Project Checkpoint</th>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>1</strong> <br>
        9/3<br>9/4
    </td>
    <td style="text-align: left;">
        <b>Intro to PCB and Schematics</b><br><br>
        Intro to the class, PCBs, KiCad, and using KiCad's schematic editor.
    </td>
    <td>
        <ul>
        	<li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1_WpjAtmyzuS9GUMBTAqdr_m3CKrjq7B2jTPNEdKDj6Q/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a>
            </li>
            <li style="margin-top: 10px;"><a href="{{ site.baseurl }}/notes/note1">Reading (Intro to PCBs)</a> </li>
            <li style="margin-top: 10px;"><a href="{{ site.baseurl }}/notes/note2">Reading (Schematics)</a> </li>
        </ul>
    </td>
    <td class="lab">
            <a href="{{ site.baseurl }}/labs/kicad_install">Install KiCad</a> <br><br>
            <!-- <a href="https://ieee.berkeley.edu/hope-kicad-install/"> Install KiCad</a><br><br> -->
            <a href="{{ site.baseurl }}/labs/lab1">Light Sensor Schematic</a>
    </td>
    <td>
        Intro to HOPE Quiz - Bcourses
    </td>
    <td>
        <a href="{{ site.baseurl }}/project-logistics">Project Logistics</a> <br><br>
        <a href="https://docs.google.com/document/d/1smVeWLNiplKkxcA6GZ_3y53MKBoSkndNkYT-nEIYHTI/edit">Project Spec</a> <br><br>
        <a href="https://docs.google.com/spreadsheets/d/1ZZAnW61lbqi8A5PHymeQs3MktsaBvQEssZroThjktFo/edit?usp=sharing&amp;ref=ieee.berkeley.edu"> BOM Template</a> <br><br>
        <a href="https://classroom.github.com/a/wL2dZu3n">Github Classroom</a> <br><br>
        <a href="{{ site.baseurl }}/github-desktop">Git Setup</a> <br><br>
    </td>
</tr>

<tr>
    <td style="text-align:center;"> <!-- Week -->
        <strong>2</strong> <br> 
        9/10<br>9/11
    </td>
    <td style="text-align: left;"> <!-- Topic -->
        <b>Footprints and Layout</b><br><br>
        Schematics to physical layout. Footprints, basic placement, and routing. 
    </td>
    <td> <!-- Reference -->
        <ul>
            <li style="margin: 15px 0px 15px 0px;">
        <a href="https://docs.google.com/presentation/d/1ZEYT3n4YUe5rT5fIwE1vpuHBZgOFiZS5qvi10xDh4Ac/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a> </li>
            <li style="margin: 15px 0px 15px 0px;"><a href="{{ site.baseurl }}/notes/note2">Reading (Schematics)</a></li>
        </ul>
    </td>
    <td class="lab"> <!-- Lab -->
        <a href="{{ site.baseurl }}/labs/lab2a">Light Sensor Components</a> <br><br>
        <a href="{{ site.baseurl }}/labs/lab2b">Light Sensor Layout</a>
    </td>
    <td> <!-- Lab Checkoff Due -->
        Light Sensor Schematic <br> - Due 9/12
    </td>
    <td> <!-- Project Checkpoint -->
    </td>
</tr>

<tr>
    <td style="text-align:center;">
        <strong>3</strong> <br> 
        9/17<br>9/18
    </td>
    <td style="text-align: left;">
               <b>Understanding Components</b><br><br>
        Real components to their symbol and footprint.
    </td>
    <td>
        <ul>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1O05Crc2QumDudakWkuBr-LM2nKU485MrZpWf1tg22tM/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a> </li>
        </ul>
    </td>
    <td class="lab">
        <a href="{{ site.baseurl }}/labs/lab3">USB Charger Components</a> <br><br>
        <!-- <a href="https://ieee.berkeley.edu/usb-charger-components">USB Charger Components</a> -->
    </td>
    <td>
        Light Sensor Components+Layout <br> - Due 9/19
    </td>
    <td>
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>4</strong> <br> 
        9/24<br>9/25
    </td>
    <td style="text-align: left;">
        <b>PCB Requirements</b><br><br>
        Overview of the PCB design and manufacturing process, and how it relates to engineering requirements.
    </td>
    <td>
        <ul>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1szEkc9CNWQVS2_0T3ZBreltsSnQH1pim4ilX3dekydc/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a></li>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1_LhTxAqtXAgTtaF7BMxn-zAdomglfNoVxemuDgUhpzw/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Symbol Creation Slides</a></li>
        </ul>
    </td>
    <td class="lab">
        <a href="{{ site.baseurl }}/labs/lab4">USB Charger Schematic</a>
        <!-- <a href="https://ieee.berkeley.edu/usb-charger-part1/">USB Charger Schematic</a> -->
    </td>
    <td>
        USB Charger Components <br> - Due 9/26
    </td>
    <td>
        <a href="http://berkie.ee/hope-fa25-project-group-submission">Project Groups</a> 
        <br> - Due 9/26
        <br> - (3 people minimum)<br>
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>5</strong> <br> 
        10/1<br>10/2
    </td>
    <td style="text-align: left;">
        <b>Microcontroller Basics</b><br><br>
        Introduction to microcontrollers, common features, and basic tips on adding them to PCBs
    </td>
    <td>
         <ul>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1CJfPpZ0wZff7xSfjeDne1GJ4E7e8GdqBduB-JG1Kv68/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a></li>
        </ul>
    </td>
    <td class="lab">
        <a href="{{ site.baseurl }}/labs/lab5">USB Charger Layout</a>
        <!-- <a href="https://ieee.berkeley.edu/usb-charger-layout/">USB Charger Layout</a> -->
    </td>
    <td>
        USB Charger Schematic <br> - Due 10/3
    </td>
    <td>
<a href="http://berkie.ee/hope-fa25-project-proposal-submission">Project Proposal</a>
    <br> - Due 10/3
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>6</strong> <br> 
        10/8<br>10/9
    </td>
    <td style="text-align: left; line-height: 30px;">
        <b>Assembly and Soldering</b><br><br>
        Practical assembly and soldering skills.
    </td>
    <td>
        <ul>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1UOW9OISqjNoI4p-HWpmuwn0rZM6dTMwDFNixltQbm-8/edit">Slides</a></li>
            <li style="margin: 15px 0px 15px 0px;"><a href="{{ site.baseurl }}/notes/note3">Reading (Creating Footprints)</a></li>
        </ul>
    </td>
    <td class="lab">
		Soldering Practice
    </td>
    <td>
        USB Charger Layout <br> - Due 10/10
    </td>
    <td>
        Proposal Review
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>7</strong> <br> 
        10/15<br>10/16
    </td>
    <td style="text-align: left;">
        <b>Advanced Layout and Passives</b><br><br>
        General layout process and overview of concerns. Non-ideal passives. 
    </td>
    <td>
        <ul><li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/12JF1bfG0X4mbw5ZZFWQvI6EWk4TB9M_f-vcO1WBV-I8/edit#slide=id.g11f980f9a13_1_191">Slides</a></li>
        <li style="margin: 15px 0px 15px 0px;"><!--<a href="https://ieee.berkeley.edu/hope-assembly/">Extra Videos</a>--> Extra Videos</li></ul>
    </td>
    <td class="lab">
        Project Work Session
    </td>
    <td>
        Hands on: Soldering <br> - Due 10/17
    </td>
    <td>
        Project Work Session
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>8</strong> <br> 
        10/22<br>10/23
    </td>
    <td style="text-align: left;">
        <strong>USB Hands-On Experience</strong><br><br>
        Assemble a PCB based on the USB Charger lab, and use it to charge your phone. 
    </td>
    <td>
    </td>
    <td class="lab">
        <a href="https://docs.google.com/presentation/d/10QwwdUPcAvdNy7LkakU-zVrh70OtulW7V5JNu-0g_cg/edit#slide=id.gcb501ed038_0_0">USB Charger Hands-On Instructions</a><br>
    </td>
    <td>
    </td>
    <td>
        Project BOM &amp; Schematic <br> - Due 10/21
    </td>
    
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>9</strong> <br> 
        10/29<br>10/30
    </td>
    <td style="text-align: left;">
        <b>Project Design Review</b>
    </td>
    <td>
    </td>   
    <td class="lab">
Project Design Review in Class<br>
        <a href="{{ site.baseurl }}/project-logistics">Design Review Requirements</a>
    </td>
    <td>
        Hands on: USB Charger <br> - Due 10/31
    </td>
    <td>
        Project Layout <br> - Due 10/31
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>10</strong> <br> 
        11/5<br>11/6
    </td>
    <td style="text-align: left;">
        <b>Ordering, Testing, and Bringup</b><br><br>
        The last bits of what you need to get a working PCB. 
    </td>
    <td>
        <ul><li style="margin: 15px 0px 15px 0px;">
        <a href="https://docs.google.com/presentation/d/1P7q-aZrW74vWJZ5W2cMZ2pb7XZuToVQ3T6C_J3QnbIw/edit">Slides</a>
		</li></ul>
    </td>
    <td class="lab">
        Project Worksession
    </td>
    <td>
    </td>
    <td>
        <strong>FINAL PCB files <br> - Due 11/6 (Thursday)</strong>
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>11</strong> <br> 
        11/12<br>11/13
    </td>
    <td style="text-align: left;">
        <b>PCB Manufacturing</b><br><br>
        The PCB manufacturing process, and how it affects layout. Outputs for manufacturing. 
    </td>
    <td>
        <ul>
            <li style="margin: 15px 0px 15px 0px;"><a href="https://docs.google.com/presentation/d/1gijMn5mIbhD0eUVxNSDjSfw6dI_Jonb3ylOAnf0B87k/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a></li>
            <li style="margin: 15px 0px 15px 0px;"><a href="{{ site.baseurl }}/notes/note4">Reading (Layout Tips)</a></li>
            <li style="margin: 15px 0px 15px 0px;"><a href="{{ site.baseurl }}/notes/note5">Videos (PCB Manufacturing)</a></li>
            <!-- <li style="margin: 15px 0px 15px 0px;"><a href="https://ieee.berkeley.edu/hope-pcb-manufacturing/">Video</a></li> -->
        </ul>
    </td>
    <td class="lab">
        <a href="{{ site.baseurl }}/labs/lab8">Trinket Lab</a>
	    <!-- <a href="https://ieee.berkeley.edu/hope-trinket-lab/">Trinket Lab</a> -->
    </td>
    <td>
        Trinket Lab <br> - Due 11/25
    </td>
    <td>

    </td>

</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>12</strong> <br> 
        11/19<br>11/20
    </td>
    <td style="text-align: left;">
        <strong>Fun Miscellaneous Topics</strong><br><br>
    </td>
    <td>
            <ul><li style="margin: 15px 0px 15px 0px;">
        <a href="https://docs.google.com/presentation/d/1bOsTk5C67lthT3bNcFUVJ-5W1JC66FXKLbewiVcJpm0/edit?usp=sharing&amp;ref=ieee.berkeley.edu">Slides</a>
		</li></ul>
    </td>
    <td class="lab">
    </td>
    <td>
        Trinket Lab <br> - Due 11/25
    </td>
    <td>
        Project Assembly
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>13</strong> <br> 
        12/3<br>12/4
    </td>
    <td style="text-align: left;">
        <b>Guest Lecture</b>
    </td>
    <td>
    </td>
    <td class="lab">
            <a href="http://berkie.ee/hope-fa25-feedback"> End-of-Semester Feedback</a> <br> - Due 12/19 <br>
    </td>
    <td>
            <a href="http://berkie.ee/hope-fa25-project-contribution"> Project Contribution</a> <br> - Due 12/19 <br>
    </td>
    <td>
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--><tr>
    <td style="text-align:center;">
        <strong>14</strong> <br> 
        12/12
    </td>
    <td style="text-align: left;">
        <b>Final Project Showcase</b>
    </td>
    <td>
    </td>
    <td class="lab">
    </td>
    <td>
    </td>
    <td>
    </td>
</tr><!--kg-card-end: html--><!--kg-card-begin: html--></tbody></table>
