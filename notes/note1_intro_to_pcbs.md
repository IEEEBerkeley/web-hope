---
layout: page
title: Introduction to PCBs
nav_exclude: true
description: Introduction to PCBs
permalink: /notes/note1
---







<div class="hero hero-mini">
<h1>HOPE: PCB Introduction</h1>
</div>
<article>
<!--kg-card-begin: html--><div><!--kg-card-end: html--><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div><!--kg-card-end: html--><p><strong>Why might you want to learn about PCB design? </strong><br>PCBs are an essential component in electronics. They can be found everywhere, from your phone to your rice cooker, your electric scooters to cars and buses and trains and possibly anything else you can think of. Learning how to make your own PCBs is an essential skill for electrical engineers, researchers, makers and of course, the college student looking forwards to joining the hardware team in one of their school's engineering project clubs. </p><p><strong>Course (recommended) prerequisites</strong>:<br>Basic understanding of electricity, electronic circuits, and their diagrams, as well as some experience working with actual electronic hardware. </p><!--kg-card-begin: html--><br><img src="/assets/note1/pcb.png" alt="stylized PCB" style="width: 80%; margin: auto; display:block"> <br><!--kg-card-end: html--><hr><!--kg-card-begin: markdown--><h1 id="whatisapcb">What is a PCB?</h1>
<p>Certainly a pertinent question for those looking to learn about how to make them. The acronym <strong>PCB</strong> stands for: <strong>P</strong>rinted <strong>C</strong>ircuit <strong>B</strong>oard. <small><small>why was this name chosen?</small></small> Very simply: a PCB is a <em>board</em> that implements a <em>circuit</em> and was <em>printed</em>, somehow. More information about the manufacturing of PCBs will be covered later. Now, to properly answer the original question, we will answer the following, related question:</p>
<h2 id="whatdoesapcbdo">What does a PCB do?</h2>
<p>The PCB, as its name implies, is a <strong>circuit</strong> <em>board</em>. In other words, a PCB is a kind of board that implements the <em>connections</em> <small><small><small>and sometimes even components</small></small></small> of an electrical circuit, as well as providing a fixed form and structure. The electrical connections between components are made inside of a stiff board; the PCB also provides the connection pads for the components to be both mechanically and electrically attached to the board. In this way it can keep things neat and tidy but also <em>simple</em>.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note1/pcbcir1.gif" alt="simple single-sided PCB gif" style="width: 80%; margin: auto; display:block"> <br><!--kg-card-end: html--><p></p><!--kg-card-begin: markdown--><h3 id="pcbalternatives">PCB Alternatives</h3>
<p>Now, there are certainly ways to implement electronic circuits without PCBs. Back before the advent of the PCB, there was, well, just wires. Behold, point-to-point wiring in an old-timey TV:</p>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note1/image-2.png" alt="old tv wiring" style="width: 60%; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Sometimes, using a solid substrate to provide support for the connections is a good idea (wire wrap board):</p><!--kg-card-begin: html--><br><img src="/assets/note1/image-1.png" alt="wire wrap" style="width: 60%; margin: auto; display:block"> <br><!--kg-card-end: html--><p>or perhaps you are in a bit of a rush and just need a single <strong>IC<em> </em></strong>to work, so you attempt a <em>deadbug:</em></p><!--kg-card-begin: html--><br><img src="/assets/note1/image-3.png" alt="deadbug" style="width: 60%; margin: auto; display:block"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><h4 id="littlebreadboardhistory">Little Breadboard History</h4>
<p>You've probably been introduced to electronics with the infamous white plastic <em>breadboard</em>:</p>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note1/half_size_breadboard.jpg" alt="breadboard" style="width: 45%; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Do you know <em>why</em> they are called "breadboards"? Well, back before these nice little spring-hole breadboards became the defacto standard for electrical prototyping, hobbyists who wanted to build circuits would use a nice solid wooden board to hold their components and help them make the connections. Drill some holes, add metal strips for power terminals, and you'd have a great foundation to work on. And what better option than their mother's breadboard?</p><!--kg-card-begin: html--><br><img src="/assets/note1/image.png" alt="literal bread board" style="width: 45%; margin: auto; display:block"> <br><!--kg-card-end: html--><h2 id="literally-what-is-a-pcb"><em>Literally</em>, <strong>what </strong>is a PCB?</h2><!--kg-card-begin: markdown--><p>TL;DR answer: A PCB is a copper and fiberglass sandwich. The fiberglass part provides stiff structure, while the copper provides the electrical connectivity.</p>
<p>More details will come in the future dedicated to PCB manufacturing details.</p>
<!--kg-card-end: markdown--><figure class="kg-card kg-image-card"><img src="/assets/note1/image(1).png" class="kg-image" alt="" loading="lazy" width="1000" height="189"></figure><hr><!--kg-card-begin: markdown--><h1 id="pcbdesigntools">PCB Design Tools</h1>
<p>Back before computers were commonplace, PCBs often were designed by hand, and every step of the process had to be verified manually. Thankfully, these days there exists many ECAD (Electronic Computer Aided Design) tools for designing PCBs, ranging from completely free (some even completely online!):</p>
<ul>
<li><a href="https://upverter.com/?ref=ieee.berkeley.edu">Altium Upverter</a> (online)</li>
<li><a href="https://easyeda.com/?ref=ieee.berkeley.edu">EasyEDA</a> (online)</li>
<li><a href="https://circuitmaker.com/?ref=ieee.berkeley.edu">Circuit Maker</a></li>
<li><a href="https://www.kicad.org/?ref=ieee.berkeley.edu">KiCAD</a></li>
<li>and many more...</li>
</ul>
<p>to expensive industry professional tools:</p>
<ul>
<li>Altium Designer</li>
<li>Cadence Allegro</li>
<li>Mentor Graphics Xpedition</li>
<li>and many more...</li>
</ul>
<p>There are even integrated Mechanical CAD and PCB ECAD tools, such as</p>
<ul>
<li><a href="https://www.autodesk.com/products/fusion-360/overview?ref=ieee.berkeley.edu">Autodesk Fusion360</a></li>
<li>Dassault Systemes Solidworks</li>
</ul>
<p><small><small>This is by no means an exhaustive list, but just a small sampling of avaliable tools.</small></small></p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><p>In this online HOPE series, we will be using <a href="https://www.kicad.org/?ref=ieee.berkeley.edu"><strong>KiCAD</strong></a>, a free, open source PCB ECAD. We suggest using this tool if you would like to follow along with the "hands on" aspect. Of course, you are free to use whatever program you would like, though note that there may be important differences in tool workflow. Occasional glimpses into other tools may be provided in the future lessons.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="basicpcbdesignflow">Basic PCB Design Flow</h1>
<p>A very important part of PCB design is <em>when</em> the PCB design tools become relevant in a project. In the typical PCB design process, <em><strong>the basic circuit is already designed</strong></em>. That is,</p>
<ul>
<li>the desired function of the circuit can be explicitly expressed</li>
<li>a rudimentary schematic of the circuit exists</li>
<li>essential parts of the design have already been researched/decided/tested<br>
before the new project is created in your ECAD.</li>
</ul>
<p>The PCB, afterall, is in some ways a finalizing component of an electric project. For the PCB itself, it is difficult and possibly even impossible to rework mistakes in either electrical or mechanical aspects. And as for the tools for creating PCBs, they are generally poor options for verifying circuit behavior, especially if digital components are involved. In this way, you should expect a lot of work to happen <em>before</em> you even jump into the schematic editor of the PCB ECAD.</p>
<p>Once in the PCB ECAD, the general process looks like so:</p>
<ol>
<li>Create schematic</li>
<li>Assign footprints (?)</li>
<li>Import to PCB layout tool</li>
<li>Group and arrange components</li>
<li>Route Traces</li>
<li>Repeat 4-5 a few times</li>
<li>Create manufacturing outputs</li>
</ol>
<p>Don't understand what certain steps mean? No worries, just follow along as the HOPE online series goes through the whole process.</p>
<!--kg-card-end: markdown--><hr><!--kg-card-begin: markdown--><h1 id="nexttime">next time:</h1>
<p><strong>Schematics and Broken Abstraction</strong><br>
<small><small>the first one with "content" hooray</small></small></p>
<!--kg-card-end: markdown--><hr><!--kg-card-begin: markdown--><p>For the few interested in the history of circuit boards:<br>
<a href="https://www.mclpcb.com/history-of-pcbs/?ref=ieee.berkeley.edu">https://www.mclpcb.com/history-of-pcbs/</a><br>
<a href="https://www.acdi.com/a-peek-at-the-history-of-pcbs/?ref=ieee.berkeley.edu">https://www.acdi.com/a-peek-at-the-history-of-pcbs/</a></p>
<!--kg-card-end: markdown--><p>Gif source:</p><figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://technologystudent.com/pcb/pcb1a.htm?ref=ieee.berkeley.edu"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Printed Circuit Boards - Introduction</div><div class="kg-bookmark-description">This site provides a wealth of technology information sheets for pupils and teachers</div><div class="kg-bookmark-metadata"><span class="kg-bookmark-author">Introduction</span></div></div><div class="kg-bookmark-thumbnail"><img src="/assets/note1/741aa.gif" alt=""></div></a></figure><!--kg-card-begin: html--></div><!--kg-card-end: html-->
</article>