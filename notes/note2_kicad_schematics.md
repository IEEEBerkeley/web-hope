---
layout: page
title: KiCad Schematics
nav_exclude: true
description: KiCad Schematics
permalink: /notes/note2
---






<div class="hero hero-mini">
<h1>HOPE: KiCad Schematics</h1>
</div>
<article>
<!--kg-card-begin: html--><div><!--kg-card-end: html--><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div><!--kg-card-end: html--><p>For the first few classes, the focus will be on becoming familiar with HOPE's PCB tool of choice: KiCad. Follow instructions in the Lecture 1 <a href="https://docs.google.com/presentation/d/1_WpjAtmyzuS9GUMBTAqdr_m3CKrjq7B2jTPNEdKDj6Q/edit?usp=sharing&amp;ref=ieee.berkeley.edu">slides</a> to download KiCad 6.</p><hr><p>Starting KiCad, you should be greeted with the main <strong>Project Manager</strong> window: </p><!--kg-card-begin: html--><br><img src="/assets/note2/Screen-Shot-2021-09-08-at-12.07.10-AM.png" alt="KiCad Project Manager Window" style="width:75%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><p>This window serves as the hub for the files and tools you need for any ECAD project in KiCad. When first started, the left side pane and main body of the window would be blank, as in the image above. </p><p>The left side "Project Files" pane serves as the <em>project tree view</em>. KiCad projects are maintained as a folder directory, and the active project's directory is shown in this side pane. PCB files can be opened in their respective KiCad sub-programs through this side pane with a double-click. </p><p>The row of large icons is a list of tools that make up KiCad. KiCad can be thought of as a collection of "independent" programs that make up the features of an entire PCB ECAD. The programs are:</p><!--kg-card-begin: html--><table class="tableblock frame-all grid-all" style="
width:80%; margin: auto
"><tbody><tr><td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong><u>Schematic Editor</u></strong></p>(Eescheema)

</td> 
<td class="tableblock halign-left valign-top"><p class="tableblock">For creating and editing schematics. Most PCB designs start here.<br><br> Note: This program was awkwardly called 'Eescheema' in KiCad 5.1 and earlier, so you may still see the Schematic Editor refered to as such in online resources.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">2</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>Symbol Editor</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Symbol editor and symbol library manager. Often used to make and manage custom symbols that aren't found in KiCad's default symbol library.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">3</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong><u>PCB Editor</u></strong></p>(PCBNew)</td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Board layout editor. You will likely be spending most of your time in this editor.<br><br> Note: This program was awkwardly called 'PcbNew' in KiCad 5.1 and earlier, so you may still see the PCB Editor refered to as such in online resources.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">4</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>Footprint Editor</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Footprint editor and footprint library manager. Often used to make and manage custom footprints that aren't found in KiCad's default footprint library.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">5</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Gerber Viewer</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Gerber and drill file viewer. Gerber and drill files are the files sent to manufacturers to produce your PCBs.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">6</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Image Converter</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Tool to build a footprint or a component from
a B&amp;W bitmap image to create logos.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">7</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Calculator Tools</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Tool to calculate track widths, and many other
things.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">8</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Drawing Sheet Editor</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Schematic drawing sheet and border editor. Used to edit the page layout and format (ie. page size, borders) of your schematics.</p></td></tr></tbody></table><!--kg-card-end: html--><p>Most of your time spent when developing a PCB will be in the Schematic Editor and PCB Editor. </p><p>The left toolbar consists of standard New/Open/Save buttons: </p><!--kg-card-begin: html--><br><img src="/assets/note2/tool.png" alt="KiCad Project Window Toolbar" style="width:75%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><!--kg-card-begin: markdown--><p>Their functions, from top to bottom:</p>
<ul>
<li>New Project</li>
<li>Open Project</li>
<li>Zip Up Project Directory</li>
<li>Unzip Project Files from a .zip</li>
<li>Refresh project tree</li>
<li>Reveal project files in Explorer/Finder</li>
</ul>
<p>These functions can also be accessed through the standard program part at the top (File -&gt; New, etc.)</p>
<!--kg-card-end: markdown--><p>Creating a new project creates both a new schematic file and board layout file in your project tree, with the same name that you chose for your project. </p><!--kg-card-begin: html--><br><img src="/assets/note2/Screen-Shot-2021-09-08-at-12.18.23-AM.png" alt="KiCad Project Directory Example" style="width:45%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><p>Note that on your actual computer, there will be a folder with the project name where you saved your project, with &nbsp;<em><code>.kicad_pro</code> , </em><code>.kicad_sch</code> , and <code>.kicad_pcb</code> files inside. </p><!--kg-card-begin: markdown--><h1 id="schematiceditor">Schematic Editor</h1>
<!--kg-card-end: markdown--><p>When you first start Schematic Editor, you may encounter this dialog box:</p><!--kg-card-begin: html--><br><img src="/assets/note2/configure_global_symbol_library.png" alt="KiCad Configure Global Symbol Library Window" style="width:75%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><p>Use the default option (Copy default global symbol library table) and continue. If this is not available as an option, this means the default global symbol library table was not installed with KiCad, which is known to occur during some Mac installations. If this is the case, ask an instructor for assistance.</p><p>This is the main window of Schematic Editor: </p><!--kg-card-begin: html--><br><img src="/assets/note2/Screen-Shot-2021-09-08-at-12.33.29-AM.png" alt="KiCad Schematic Editor" style="width:100%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><p>The basic concept of using this program (or any other PCB ECAD schematic editor) is simple: take your hand-drawn diagram of your circuit and recreate it. If you have used some kind of digital schematic editor before, such as the one in LTSpice, this should feel somewhat familiar. </p><blockquote>While search up help for the Schematic Editor in KiCad, you may find it occasionally referenced as 'Eeschema'. This was the original name for the schematic editor sub-program of KiCad, before the decision was made in KiCad 6 to just called it 'Schematic Editor'.</blockquote><hr><h1 id="schematic-basics">Schematic Basics</h1><!--kg-card-begin: markdown--><p>Schematics are meant to be diagrams of an electrical circuit that are:</p>
<ul>
<li>Human Readable
<ul>
<li>Neat - focus on visual clarity</li>
<li>Consistent
<ul>
<li>Component representation</li>
<li>Connectivity representation</li>
</ul>
</li>
</ul>
</li>
<li>Provide Accurate Circuit Description
<ul>
<li>Show all components</li>
<li>Express full connectivity</li>
<li>Contain additional information to assist the physical layout</li>
</ul>
</li>
</ul>
<p>A blueprint is a good analogy. Without a good, clear, and thorough blueprint, the building the blueprint is for will likely be built inadequately, or even worse, not work at all.</p>
<!--kg-card-end: markdown--><hr><!--kg-card-begin: markdown--><p>We assume that you are used to working with electrical components and schematics already, and understand the abstracted swiggly line in a schematic as a physical resistor. In making PCBs we use the following three terms to differentiate which "form" of an electrical component we are talking about:</p>
<ul>
<li><strong>(part) symbol</strong> belongs on the schematic</li>
<li><strong>footprint</strong> belongs in the board layout</li>
<li><strong>component/part</strong> refers to it as the physical object</li>
</ul>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h2 id="ecadschematiccoreideas">ECAD Schematic Core ideas:</h2>
<ol>
<li><strong>Everything is built on a grid</strong>: Like many other drawing programs, Schematic Editor is built on a grid. Everything in the schematic, from the electrical/part symbols to the wires and even text notes adhere to the grid. You can change the grid size, the grid units, and the grid visibility if you wish, but since connections between components must also be drawn on the grid, it is better to <strong>leave the grid size and units settings alone</strong>.</li>
<li><strong>Electrical Components are represented by abstract Part Symbols</strong>: This is a concept you should be familiar with, but when working with PCBs, there is an additional, important feature: most symbols represent <em>real parts</em>, which are often abstracted in symbol form as boxes with pins.</li>
<li><strong>Symbol Pins are special</strong>: the pins in a symbol are stuck to it and have special properties compared to the connecting wire in the schematic editor. Real components often have constraints on their pins, and such general descriptions of pins can be set in the part symbol. KiCad uses these special pin properties to detect any potential bad connections in your schematic when your run the <em>Electric Design Rules Checker</em>.</li>
<li><strong>Symbols are found in Symbol Libaries</strong>: By default, KiCad allows you only to place parts from its <em>global symbol library table</em>. This is a list of collections ("libraries") of part symbols, with each library organized such that all the parts in it are related to each other in some way, such as all capacitors, or all from a certain company. Users such as yourself can create your own symbol libraries, and designate them to be either part of the <em>global symbol library table</em> (accessable in any of your projects) or <em>project symbol library table</em> (accessable in only the current project).</li>
<li><strong>Computer understands schematic as a netlist</strong>: A <em><strong>netlist</strong></em> is essentially a textfile listing which component is connected to each other. Specifically, it is a list of <em><strong>nets</strong></em>, which are the connection between any set of component <em>pins</em>.</li>
</ol>
<!--kg-card-end: markdown--><p>Just like how the wires in schematics can be whatever shape and still mean the same connections, the netlist is like the ultimate minimization of that idea. The reason for this is because all the connection in a schematic implies is that these component pins are connected together, but in no way specifies <em>how</em> they should be connected <em>physically</em>. The art of PCB layout is figuring out that part. </p><!--kg-card-begin: html--><br><img src="/assets/note2/image-5.png" alt="example of a net in a netlist" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><hr><h1 id="making-schematics">Making Schematics</h1><p>This lesson will go through the basic schematic creation process, and thus will not cover every single aspect of Schematic Editor in detail. KiCad comes with a comprehensive wiki-style manual which we highly recommend that you reference should you be confused with program specifics. You can pull up the (online) manual for any of KiCad's program through the "Help" menu in the Top menu bar: </p><!--kg-card-begin: html--><br><img src="/assets/note2/image-13.png" alt="locating the manual" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><h3 id="navigation">Navigation</h3><!--kg-card-begin: html--><table class="tableblock frame-all grid-all" style="width: 60% ; margin: auto"><tbody><tr><td class="tableblock halign-left valign-top"><p class="tableblock">Left Click</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">General selection</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Right click</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Pop-up menu</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Middle-click</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Pan</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Scroll Wheel</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Zoom In/Out</p></td></tr>
</tbody></table><!--kg-card-end: html--><h3 id="basics">Basics</h3><blockquote>Useful tip: &nbsp;Hover over any icon in the toolbar to see a pop-up describing what each icon does.</blockquote><p>As with any other schematic, you start with placing down some components. You can switch to "Place Symbol" by finding the following icon in the top menu bar or right side bar:</p><!--kg-card-begin: html--><br><img src="/assets/note2/add_symbol-1.png" alt="place symbol icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Click anywhere in the schematic while the "Place Symbol" tool is enabled to open up the "Choose Symbol" window. Any symbol in a library associated with the current project will be selectable. You can search for the part symbol you want with the filter bar. Recently used symbols will conveniently show up at the top. </p><!--kg-card-begin: html--><br><img src="/assets/note2/Add_a_symbol.png" alt="KiCad Symbol Selection Window" style="width:75%; margin: auto; display:block"> <br>
<!--kg-card-end: html--><p>After selecting a symbol you will be able to place it down in your schematic. </p><!--kg-card-begin: markdown--><blockquote>
<p>Fun search tidbit:  this search-bar supports Regular Expressions and wildcards!</p>
</blockquote>
<!--kg-card-end: markdown--><p>An important part of any schematic are power port symbols, such as supply power and system ground. KiCad treats these as special symbols and has its own special tool to access just the "power" library. (These symbols are also in the regular 'Choose Symbol' menu above.)</p><!--kg-card-begin: html--><br><img src="/assets/note2/power_symbol.png" alt="place power symbol icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Once you've place your symbols on the schematic, you will need to connect them with wires. Switch to the "Place Wire" tool by finding the following icon in the right side bar. The icon on your system may look like the one below, or it may look like a green stick. (The blue stick is a different tool!)</p><!--kg-card-begin: html--><br><img src="/assets/note2/Screen-Shot-2021-09-08-at-5.03.04-PM.png" alt="place wire icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>With the tool selected, click anywhere to start placing a wire. While wire-placing is active, you can click again to make a junction, allowing you to change the direction of the wire. Connect the wire to a symbol pin, or double-click in an empty space to terminate the wire. You can cancel the wire placement by hitting the "Esc" key or through the right-click menu. </p><!--kg-card-begin: html--><br><img src="/assets/note2/688GMgs5Pd.gif" alt="routing" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><blockquote>
<p>By default, wire movement is restricted to straight lines and right-angle turns. This is to keep your schematic neat, but there is an option to disable this: can you find where it is?</p>
</blockquote>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><p>As with any tool program, hotkeys (or "shortcuts") exist to speed-up your workflow. You can open up the hotkey list for any KiCad program through the "Help" menu or with <code>Ctrl+F1</code>. We recommend getting used to using shortcuts, it will considerably speed up your design process.</p>
<!--kg-card-end: markdown--><p>In addition to wires, you can also directly add a component pin to a net with a <strong>net label</strong>. KiCad treats multiple wires and pins that has the same label as all electrically connected together, without needing a wire actually connecting all of the section. The power symbols are basically a special type of net label. You are probably familiar with how you can use the ground symbol to show that two different parts of your schematic are connected together via ground, and this is the exact same idea, but more generalized. </p><!--kg-card-begin: html--><br><img src="/assets/note2/Screen-Shot-2021-09-08-at-5.04.33-PM.png" alt="place net label icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Net labels are very useful for keeping your schematic neat and readable, and are also used to <em>name nets</em>. It'll become more obvious why this is useful later, but for now you can ponder why a net named "servo1_output" may be better than a auto-generated name like "Net-(C2-Pad1)". </p><!--kg-card-begin: html--><br><img src="/assets/note2/image-29.png" alt="net label usage example" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><h3 id="manipulation">Manipulation</h3><p>Sometimes a symbol has to be moved or rotated, or wires re-organized. Any object can be selected with a left click, and multiple objects can be selected with a click-and-drag. All manipulation options can be found in the right-click menu. Double-clicking on editable object (such as symbols) will bring up their properties. </p><p>In addition to selecting objects with a click, KiCad can also work by <em>hover selection</em>; that is, when using shortcuts, the object under your mouse cursor is your active object. This allows for fast single object editing. Please note that if an object is selected, it will always be the <em>active</em> object, whereas if there is no object selected, then the <em>active</em> object is whatever is under your mouse cursor. </p><p>The following is a short list of helpful keyboard shortcuts for manipulation of objects:</p><!--kg-card-begin: html--><table class="tableblock frame-all grid-all" style="
width:40%; margin: auto
"><tbody><tr><td class="tableblock halign-left valign-top"><p class="tableblock">Edit Item</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">E</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Delete Item</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Del</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Rotate Item Counter-Clockwise</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">R</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Drag Item</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">G</p></td></tr>
<tr><td class="tableblock halign-left valign-top"><p class="tableblock">Mirror X</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">X</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Mirror Y</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Y</p></td></tr>
<tr><td class="tableblock halign-left valign-top"><p class="tableblock">Move Schematic Item</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">M</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Copy Objects</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Ctrl+C (Cmd+C)</p></td></tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Paste Objects</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Ctrl+V (Cmd+V)</p></td></tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Drag wire (wire-like objects only)</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">G</p></td></tr></tbody></table><!--kg-card-end: html--><!--kg-card-begin: html--><br><img src="/assets/note2/CVObbnwWRq.gif" alt="manipulating a symbol" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>Dragging existing wires with <strong>'G'</strong> in the Schematic Editor is somewhat non-intuitive, and the wires do not stay perpendicular/horizontal when dragged in certain ways. You will have to add breakpoints, or junctions, in the wire manually. </p><!--kg-card-begin: html--><br><img src="/assets/note2/Y9GJdIl5EL.gif" alt="adjusting a wire" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>In both KiCad's schematic editor and board layout editor, your cursor will actually snap to the grid. This can sometimes make selecting things precisely difficult. In cases when your selection might be ambiguous, KiCad will prompt you with a dialog such as this: </p><!--kg-card-begin: html--><br><img src="/assets/note2/image-31.png" alt="clarify selection pop-up" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><h3 id="annotation">Annotation</h3><p>Now your schematic has really taken shape, but all your symbols have unfilled <strong>part designators</strong>. These are short names to help both KiCad, and you the designer, and possibily anyone else working with your PCB, <em>identify the components</em>. The letter helps identify generally what kind of component it is, and the number is just a numerical identifier. (It is a bit easier asking for "What is Resistor 4?" than "What is component 17?")</p><p>You can find many lists of letter references online, such as <a href="https://dexpcb.com/manual/standard-reference-designators.htm?ref=ieee.berkeley.edu">this one</a>.</p><p>KiCad takes care of the designator letter, as these letters are stored in the library data of the symbol. However, the number is determined per-project, and thus completing the rest of the part designator is the job of the PCB designer. Luckily, KiCad has a "Annotate Schematic" function to auto-magically do this for you, changing those <em>R?</em> into <em>R2's</em> and <em>R3</em>'s. You can find this tool with it's icon:</p><!--kg-card-begin: html--><br><img src="/assets/note2/refdes_icon-2.png" alt="annotate schematic tool icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><blockquote>
<p>The Annotate Schematic tool assigns numbers based on symbol location in the schematic, and there are some options to change which order the number goes in. Play around with symbol placement and the sort direction to see what happens.</p>
</blockquote>
<!--kg-card-end: markdown--><h3 id="erc">ERC</h3><p>Like most other PCB eCAD, KiCad has <strong>Electrical Rule Check </strong>functionality, albeit very primitive. Straight from the Schematic Editor (Eeschema) manual: </p><blockquote>The ERC checks for any errors in your sheet, such as unconnected pins, unconnected hierarchical symbols, shorted outputs, etc. Naturally, an automatic check is not infallible, and the software that makes it possible to detect all design errors is not yet 100% complete. Such a check is very useful, because it allows you to detect many oversights and small errors.</blockquote><p>How it does this is through the <em>pins</em> of the symbols. These pins can, for example, specify they are output or input, power or bidirectional. If two incompatible pins are connected (i.e. two outputs are connected to the same net) or if a symbol's pin is left unconnected, the ERC will catch this and report an error. <strong>ERC errors will prevent you from moving on to layout</strong>, so learn to work with them. A problem in your schematic will also mean problems in your manufactured board. </p><!--kg-card-begin: html--><br><img src="/assets/note2/erc_icon-1.png" alt="ERC tool icon" style="width: auto; margin: auto; display:block"> <br><!--kg-card-end: html--><p>The point of the ERC is to prevent oversight of simple mistakes in your schematic. <strong>ERC cannot tell you whether your circuit will work or whether or not you are using a component correctly, that is your job as an engineer</strong>. </p><h1 id="conclusion">Conclusion</h1><p>This was just a short introduction to how to use KiCad's Schematic Editor. We highly suggest you look around in the official manual for more on its features, or ask an instructor if you have questions. </p><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div>

</div><!--kg-card-end: html-->
</article>
```