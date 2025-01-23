---
layout: page
title: Creating Footprints
nav_exclude: true
description: Creating Footprints
permalink: /notes/note3
---






<div class="hero hero-mini">
<h1>HOPE: Footprint Creation</h1>
</div>
<article>
<!--kg-card-begin: html--><div>     
<div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div><!--kg-card-end: html--><!--kg-card-begin: markdown--><h1 id="footprintcreation">Footprint Creation</h1>
<p>Footprints are stored in libraries just like KiCad symbols. For the component footprints you create, we recommend adding the parts to a project library.</p>
<p><strong>Note:</strong> Do <strong>NOT</strong> add standard passives to your library (i.e. external capacitors, resistors for ICs). <strong>DO</strong> add the passive if it has a special shape (i.e., a high wattage resistor).</p>
<blockquote>
<p>Something to think about: Why might, in a collaborative environment, using project libraries instead of global libraries be a good idea?</p>
</blockquote>
<ol>
<li>Open up your footprint editor from the KiCad home window:</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image.png" alt="footprint editor" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="2">
<li>Create a new footprint Library by doing File → New Library. Make sure to select "Project" in the "Select Library Table" window.</li>
</ol>
<blockquote>
<p>Note how the footprint library is saved. A folder with a custom extension!</p>
</blockquote>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-1.png" alt="new footprint library" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="3">
<li>Create a new footprint for a part you have chosen and add it to the footprint library you had just created (KiCad will prompt you if you try saving).</li>
</ol>
<blockquote>
<p>KiCad has a bunch of simple footprint generators ("File-&gt;Create Footprint...") for standard-like footprints (and decorative layout elements), which we suggest you try out, just to know it exists. Make sure to double check the footprint it creates though!</p>
</blockquote>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-2.png" alt="new footprint" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><p>This should start you off very similarly to symbol creation, with only a reference designator (on the Front Silkscreen layer) and the footprint name (on the Front Fab layer) in an otherwise empty grid. </p><!--kg-card-begin: html--><br><img src="/assets/note3/image-3.png" alt="new footprint window" style="width: 80%; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="4">
<li>The process for creating footprints is as so:
<ol>
<li>Place and dimension component pads</li>
<li>Draw important silkscreen</li>
<li>Draw component courtyard region</li>
<li>Anything else: assembly data, 3D model</li>
</ol>
</li>
</ol>
<p><strong>You should have the component's datasheet open to the page on its physical dimensions for whatever component package you have chosen to use before starting.</strong><br>
We <em>highly</em> suggest watching <a href="https://youtu.be/ZHH4G_EWhm0?t=351&amp;ref=ieee.berkeley.edu">Digikey's Footprint Creation Tutorial</a>. Start from 5:51. If you have some time, the entire series is a good walkthrough of the KiCad/PCB design process. Note however, that the video tutorial was made using an older version of KiCad, and thus certain features have been changed since then.)</p>
<blockquote>
<p>We do not recommend remaking standard packages that already exist in the default footprint libraries KiCad provides.</p>
</blockquote>
<!--kg-card-end: markdown--><figure class="kg-card kg-embed-card"><iframe width="600" height="339" src="/assets/note3/ZHH4G_EWhm0.html" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></figure><!--kg-card-begin: markdown--><h2 id="quickfootprintwalkthrough">Quick Footprint walkthrough</h2>
<p>Some important tidbits before you begin:</p>
<ol>
<li>Make correct use of the origin to make rotation and placement more intuitive.</li>
<li>Choose a grid size that makes sense for the footprint you are making. Because this is representative of a real part, maintaining a regular grid size is unnecessary.</li>
<li>At the very least, make the relative dimensions between the pads, as well as the pad sizes, accurate to the datasheet recommendation.</li>
</ol>
<p>You may want to move the default designator and name text out of the origin before you begin.</p>
<blockquote>
<p>There are some visualization tools in the left toolbar. Toggle them on and off to see what they do, and how they might be helpful.</p>
</blockquote>
<h3 id="placingpads">Placing Pads</h3>
<ol>
<li>Just like symbol creation, we start with the pads (pins in the symbol). Notice that pad placement happens on the defined grid. One tip to make the pad placement process easier is to <em>set the grid to the desired spacing</em>.</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-5.png" alt="place pad" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="2">
<li>Opening up the pad properties opens a similar window to the pin properties found in the symbol editor, but with pad-specific features, such as pad type, shape, size, and layers. Here, you can set the position of the pad precisely. In most cases you will not need to worry about changing the layers, as the Pad type will select the right ones for you.</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-7.png" alt="pad properties" style="width: 80%; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="3">
<li>
<p>Place the rest of the pads in the correct spots. The <em>Measure</em> tool may be helpful to verify placement. Note that you can hold down the Alt key to disable grid-snap, or Ctrl to snap to 45 degree angles.</p>
</li>
<li>
<p>The next few steps will involve using the graphic tools. These work <em>exactly the same</em> in all board layers; the board layer determines what the actual result is.</p>
<ul>
<li>Put elements in the Front (or back) silkscreen layer (F.SilkS) to help visualize your part. The most important element of the silkscreen is the <em>orientation mark</em>, which is usually a dot next to the pin 1. You may find other forms for different kinds of components.</li>
<li>Draw the general body of the component in the Fabrication layers. This is a meta data layer mainly for automated assembly use, but you can use it for generating the general shape to use as a base for the graphics on other layers, such as adding a silkscreen outline or component courtyard.</li>
<li>Add a component courtyard. This is the 2D area that KiCad uses to determine whether two components will physically collide.</li>
</ul>
</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/RZUYbdby94.gif" alt="placing silkscreen track" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><ol start="5">
<li>You can change the footprint properties (name, description, keywords) and add more info, such as a 3D representation of the component, using the Footprint Properties window (Edit -&gt; Footprint Properties).</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-8.png" alt="footprint properties" style="width: 70%; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><h2 id="usingpreexistingfootprints">Using pre-existing footprints</h2>
<p>In addition to creating footprints yourself from component datasheets, you may also find component footprints (as well as symbols, or even entire part libraries such as the Digikey KiCad component library) online. There are a multitude of tools at your disposal: feel free to use any of them but make sure to always double check any footprint found online.</p>
<h3 id="howtoimportkicadfootprints">How to import KiCad footprints</h3>
<ol>
<li>Download the footprints (must be for KiCad v4+) and uncompress them if needed.</li>
<li>File → Import Footprint from KiCad File. Select the .kicad_mod footprint file that you would like to use.</li>
<li>Double check the imported footprint.</li>
<li>Save the footprint to your project footprint library.</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="/assets/note3/image-4.png" alt="importing footprints" style="width: auto; margin: auto; display:block; background-color:#FFFFFF"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><h3 id="howtoimportkicadfootprintlibraries">How to import KiCad footprint libraries</h3>
<p>This is useful for when you need an entire library of component footprints, such as Digikey's footprint library.</p>
<ol>
<li>File → Add Library (its like, the "New Library" symbol but with a plus + sign)</li>
<li>Select the footprint library folder.</li>
<li>Add the library either to the Project or Global library table.</li>
<li>Money</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div>
<!--kg-card-end: html--><!--kg-card-begin: html--></div><!--kg-card-end: html-->
</article>