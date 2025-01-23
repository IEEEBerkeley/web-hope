---
layout: page
title: Light Sensor Lab - Schematic
nav_exclude: true
description: Light Sensor Lab - Schematic
permalink: /labs/lab1
---

Light Sensor Lab - Schematic
==============

* Do not remove this line (it will not be displayed)
{:toc}

In this KiCad activity, you will draw the schematic for a PCB of an LED light sensor.  You may find our [write-up on KiCad schematics](https://ieee.berkeley.edu/hope-rd-schematics/), the reading for this week, a helpful reference.

As you go through this lab, don't hesitate to ask questions!  We're here to help you learn and understand the material.

We recommend using a mouse for all labs as it will make navigation and component placement much easier.

# KiCad Setup

Follow the instructions in [Install KiCad]({{ site.baseurl }}/labs/kicad_install)

Ask us for help if you run into any issues.

# Getting Started

1. Launch KiCad.  If you have not run KiCad since installing, you may see a dialog box similar to the one below, in which case simply click `OK`.  Otherwise, you should be seeing the main project manager window.

<img src="/assets/lab1/kicad_initial_config.png" style="border-radius: 0em" alt="KiCad initial configuration popup">

2. Make a new project by `File -> New -> Project` or by using the keyboard shortcut `Ctrl+N`/`⌘+N`.  Pick a reasonable project name (i.e. `light_sensor`) and a safe place to save your project *directory* (a folder will be created to house all your KiCad project files).

> You won't be able use KiCad (or any other PCB ECAD for that matter) as a comprehesive PCB ECAD unless you're working under the context of a project, so make sure to do this step!

# Schematic Capture

Open the 'Schematic Editor'.

<img src="/assets/lab1/kicad_create_schematic.png" style="border-radius: 0em" alt="Project manager, create schematic button">


Click `OK` if you see this dialog box (with the recommended option selected):

<img src="/assets/lab1/kicad_symbol_library_popup.png" style="border-radius: 0em" alt="Symbol library configuration popup">

If the first option is greyed out, please ask an instructor for assistance.

**Your goal is to replicate the schematic shown below**:

<img src="/assets/lab1/light_sensor_schematic.png" style="border-radius: 1em" alt="Light sensor schematic">

1.  The first thing we'll want to do in the schematic is add the critical component: *the op-amp*.  Press the `A` hotkey to add a symbol, then click anywhere to place a symbol, and press `Esc` to stop adding symbols.

    > Interested in why the op-amps come as these separate units of one part? Take a look at page 18 of the [LMC6482's datasheet](http://www.ti.com/lit/ds/symlink/lmc6482.pdf) to get some idea of why the component would be set up this way. 

    <img src="/assets/lab1/schematic_add_component.gif" alt="Schematic Add Component Animated" style="width:100%; margin: auto; display:block">

    > Go to `Help -> List Hotkeys` or press `Ctrl+F1`/`⌘+F1` to open up KiCad's built-in keyboard shortcuts cheat sheet!

    >  Note that the middle mouse can be used to pan in both the schematic and layout editor. This will help alleviate the headache of trying to scroll around both.

1.  Continue by placing the following parts to match the completed reference schematic:

    | Component | Symbol name |
    | ------- | ------ |
    | 2 capacitors | `C` or `C_small` |
    | 3 resistors  | `R` or `R_small` |
    | An LED part symbol | `LED` |
    | A potentiometer part symbol | `R_Potentiometer` |
    | A 1x3 connector part symbol | `Conn_01x03` (from the `Connector_Generic` symbol library) |

    > Press `R` with a component selected to rotate it 90° counter-clockwise.

    After placing your symbols, notice that the values of the resistors and capacitors are blank.  Ignore this for now.

1.  Wire up your components!  Press the `W` hotkey to activate the wire tool and press `Esc` to go back to the selection tool.  Repeat until the schematic is fully captured.
    + Drag placed wires by selecting or hovering over them and pressing `G`.  Delete segments by selecting or hovering over and pressing `Backspace` or `Del`, or right-click the wire for more options.
    + To create a wire that does not connect to a component on one end (a *floating wire*), double-click where you want the wire to end.  Floating wires will be useful for components that will need power or ground labels later.
    + To add labels (such as the `Vout` label in the schematic), press `L`, type in the name of your label, and press `Enter`.  Labels connect two or more nodes together without actually drawing the wire on the screen.  They are basically magic wire tunnels linked by name.

1.  Now add power symbols (arrows labeled `+3.3V` and triangles labeled `GND`) to your schematic by pressing `P`.  For this step, it may be easier to duplicate a component instead of adding multiple of the same component.  To do this, select the component you want to copy and press `Ctrl+C`/`⌘+C`.  Paste the component with `Ctrl+V`/`⌘+V`.
    > Power symbols are similar to labels in that they connect nodes together, but have the symbol there to tell you what they are at a glance.

1.  Next, add power flags to the schematic, also from the `Power` library opened when you press `P`.
    > Power flags serve to tell the Electrical Rules Checker (ERC) in subsequent steps that the pin or wire is connected to power, even if a source isn't specified.

1.  Assign values to components. The easiest way to do this is to select or hover over the component and press `V`. You can also double-click the component to open its properties or right-click and open 'Properties'. Type the appropriate value. Omit units for resistors but include units for capacitors and inductors (F for farads, H for Henries, etc.). For example, a 1kΩ resistor value would simply be `1k` and a 1 nF capacitor value would be `1nF`.

1.  Run the Electrical Rules Checker (ERC) and ensure there are no errors.  If there are, fix the listed errors in your schematic and run the ERC again, until it is error-free.

    Click this icon to run the ERC: ![erc_icon](/assets/lab1/erc_icon.png)

1.  Visually double-check your schematic to make sure it matches the reference schematic above. The ERC *does not check this for you*. 


# Check-in
Once your ERC returns no errors and your schematic matches the reference schematic, fill out the check-off form: [https://berkie.ee/hope-sp25-checkoff](https://berkie.ee/hope-sp25-checkoff)

When it's your turn, a staff member will come by, review your schematic, and ask a few questions.  If everything looks good, they will check you off for this lab.