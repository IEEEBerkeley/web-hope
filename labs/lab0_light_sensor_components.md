---
layout: page
title: Light Sensor Lab - Components
nav_exclude: true
description: Light Sensor Lab - Components
permalink: /labs/lab0
---

{:toc}

# Light Sensor Lab - Components

An essential part of making any idea into a practical reality is taking your abstract schematic symbols (which are meant to represent some electrical function but aren't tied to anything in reality) and assigning real, existing components to them. Learning where to find components and how to pick the right ones for your project is an essential skill, but the task can be overwhelming for those new to it. This activity will walk you through navigating the online marketplace Digikey.

## What is Digikey?
Digikey is an online marketplace for all manner of electronic components, and is one of the major (if not *the main*) parts distributors for electronic components. If you're making a PCB and need parts (or even a manufacturer for your PCB), Digikey is more likely than not going to have everything you need. They have tremendous amount of different kinds of available products, from the simplest, most common passives like tiny chip resistors and capacitors, to breakout boards for microcontrollers and fancy sensors, to even mechanical housings and bench test equipment.

## Searching Digikey
For the light sensor board, there are a total of 9 components:
- **1** LMC6482 Op-Amp IC *(this single part is represented by the 3 U1 symbol variants in the schematic; it has 2 op-amps in 1 package)*
- **1** LED
- **3** Resistors
- **2** Capacitors
- **1** Potentiometer
- **1** Three-pin connector

For the purposes of this exercise, we'll only walk you through the Op-Amp, resistors, and capacitors.

### Op-Amp
Let's start with the easiest item on the list: the part that already is picked out for you. The LMC6482 is the part number of a real component! In Digikey's search bar, search for 'LMC6482':

<img src="/assets/lab0/digikey-home-page.png" style="border-radius: 1em">

This should bring you to Digikey's search results:

<img src="/assets/lab0/digikey-op-amp-search1.png" style="border-radius: 1em">

Pay close attention to the structure of this annotated page:

- The yellow box contains your filters, which you can use to refine your search results
- The green box contains a set of "Top Results", which highlights the top few categories of components that match your search
- The blue box lists the categories of components that match your search
- The orange box lists the same categories of components, along with sub-categories that match your search.

We know we don't need an Integrated Circuit *Kit* (a box of assorted integrated circuits), but rather a specific LMC6482 IC, so click one of the links in the **Integrated Circuits (ICs)** category.

Once the search is refined down to a single category, Digikey will show this part filtering page:

<img src="/assets/lab0/digikey-op-amp-search2.png" style="border-radius: 1em">

We know this page might be a little intimidating, but it's structure is fairly simple.  At the top, you have filters in a horizontal table.  Below that, you have common filters, and below that, you have the list of parts that match all filters you apply.

It turns out that there are a lot of LMC6482 ICs and a lot of them look basically the same!  Luckily for us, there are a couple of important factors we can use here to filter out most of these options, the first of which being whether or not the component is **actually in stock**!  Tick that under "Stocking Options" in the Filter Options below the filter list, then click "Apply All":

<img src="/assets/lab0/digikey-common-filters.png" style="border-radius: 1em">

When searching for components, the other options can be very useful too!  In particular the "Marketplace Product" "Exclude" option removes all Marketplace products, which are items Digikey lists on their website, but are actually sold and fulfilled by another company.  We try to stay away from Marketplace products since they often have much longer lead times, and tend to make sense only for larger-scale projects.

At the time of writing this lab guide, simply filtering for stock eliminates 11 of 23 results.  However, to further filter, we can use some of the options in the filter table:

<img src="/assets/lab0/digikey-op-amp-search3.png" style="border-radius: 1em">

In this case, we used "Product Status" and "Mounting Type" to narrow the search down to two parts, which turn out to be almost identical components, which for our use case we can finally just sort by price.

Product status filters between components that are actively being manufactured, and parts that are just old stock that are being sold for people who designed things to use those parts before they became obsolete.  Thus, for a new design, especially if you're trying to make a product, you'll want to filter for active products.

As you saw in lecture today, there are two main types of component mounting: through-hole (THT), and surface-mount (SMD).  For our op-amp here, we chose through-hole for ease of assembly.


We'll want to note down somewhere what actual parts we've chosen to physically realize our schematic for reference later when assigning footprints to your symbols (first activity of lab 2!). For now, just adding the component to cart or a list will work. Later this semester we'll go over the proper way of keeping track of these components in a BOM (Bill of Materials). 