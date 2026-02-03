---
layout: page
title: Light Sensor Lab - Components
nav_exclude: true
description: Light Sensor Lab - Components
permalink: /labs/lab2a
---

Light Sensor Lab - Components
==============

* Do not remove this line (it will not be displayed)
{:toc}

An essential part of making any idea into a practical reality is taking your abstract schematic symbols (which are meant to represent some electrical function but aren't tied to anything in reality) and assigning real, existing components to them. Learning where to find components and how to pick the right ones for your project is an essential skill, but the task can be overwhelming for those new to it. This activity will walk you through navigating the online marketplace Digikey.

# What is Digikey?
Digikey is an online marketplace for all manner of electronic components, and is one of the major (if not *the main*) parts distributors for electronic components. If you're making a PCB and need parts (or even a manufacturer for your PCB), Digikey is more likely than not going to have everything you need. They have tremendous amount of different kinds of available products, from the simplest, most common passives like tiny chip resistors and capacitors, to breakout boards for microcontrollers and fancy sensors, to even mechanical housings and bench test equipment.

# Searching Digikey
For the light sensor board, there are a total of 9 components:
- **1** LMC6482 Op-Amp IC *(this single part is represented by the 3 U1 symbol variants in the schematic; it has 2 op-amps in 1 package)*
- **1** Photodiode
- **3** Resistors
- **2** Capacitors
- **1** Potentiometer
- **1** Three-pin connector

For the purposes of this exercise, we'll only walk you through the Op-Amp, resistors, and capacitors.

## Op-Amp
Let's start with the easiest item on the list: the part that already is picked out for you. The LMC6482 is the part number of a real component! In Digikey's search bar, search for 'LMC6482':

<img src="/assets/lab2a/digikey-home-page.png" style="border-radius: 1em">

This should bring you to Digikey's search results:

<img src="/assets/lab2a/digikey-op-amp-search1.png" style="border-radius: 1em">

Pay close attention to the structure of this annotated page:

- The yellow box contains your filters, which you can use to refine your search results
- The green box contains a set of "Top Results", which highlights the top few categories of components that match your search
- The blue box lists the categories of components that match your search
- The orange box lists the same categories of components, along with sub-categories that match your search.

We know we don't need an Integrated Circuit *Kit* (a box of assorted integrated circuits), but rather a specific LMC6482 IC, so click one of the links in the **Integrated Circuits (ICs)** category.

Once the search is refined down to a single category, Digikey will show this part filtering page:

<img src="/assets/lab2a/digikey-op-amp-search2.png" style="border-radius: 1em">

We know this page might be a little intimidating, but it's structure is fairly simple.  At the top, you have filters in a horizontal table.  Below that, you have common filters, and below that, you have the list of parts that match all filters you apply.

It turns out that there are a lot of LMC6482 ICs and a lot of them look basically the same!  Luckily for us, there are a couple of important factors we can use here to filter out most of these options, the first of which being whether or not the component is **actually in stock**!  Tick that under "Stocking Options" in the Filter Options below the filter list, then click "Apply All":

<img src="/assets/lab2a/digikey-common-filters.png" style="border-radius: 1em">

When searching for components, the other options can be very useful too!  In particular the "Marketplace Product" "Exclude" option removes all Marketplace products, which are items Digikey lists on their website, but are actually sold and fulfilled by another company.  We try to stay away from Marketplace products since they often have much longer lead times, and tend to make sense only for larger-scale projects.

At the time of writing this lab guide, simply filtering for stock eliminates 11 of 23 results.  However, to further filter, we can use some of the options in the filter table:

<img src="/assets/lab2a/digikey-op-amp-search3.png" style="border-radius: 1em">

In this case, we used "Product Status" and "Mounting Type" to narrow the search down to two parts, which turn out to be almost identical components, which for our use case we can finally just sort by price.

Product status filters between components that are actively being manufactured, and parts that are just old stock that are being sold for people who designed things to use those parts before they became obsolete.  Thus, for a new design, especially if you're trying to make a product, you'll want to filter for active products.

As you saw in lecture today, there are two main types of component mounting: through-hole (THT), and surface-mount (SMD).  For our op-amp here, we chose through-hole for ease of assembly.


We'll want to note down somewhere what actual parts we've chosen to physically realize our schematic for reference later when assigning footprints to your symbols (first activity of lab 2!). For now, just adding the component to cart or a list will work. Later this semester we'll go over the proper way of keeping track of these components in a BOM (Bill of Materials). 

## Resistors
If you thought there were a needless amount of versions of the LMC6482 IC, wait until you see how many different kinds of resistors there are:

<img src="/assets/lab2a/digikey-resistor-search1.png" style="border-radius: 1em">

In short, there are *tons*, so to speed things up we'll tell you exactly what you need to search for to find the reasonable resistors.  Let's take R1 and R2, our 10 kΩ resistors, for this search example.

Narrow down the product list to the kind of resistors you are familiar with by going straight to the **Through Hole Resistors** product category:

<img src="/assets/lab2a/digikey-resistor-search2.png" style="border-radius: 1em">

We can then input these options:

| Resistance | 10 kOhms |
| Tolerance | ±5% |
| Power (Watts) | 0.25W, 1/4W |

For good measure, let's also tick the "In Stock" filter before applying all the filters to our search.

<img src="/assets/lab2a/digikey-resistor-search3.png" style="border-radius: 1em">

The resulting list is much more reasonable, but let's add one more filter before selecting one.  If you've messed around with through-hole resistors enough, you'll have noticed that there's mostly 2 sizes for the standard 1/4W through-hole resistors, one smaller than the other.  Let's say we would like to use this smaller size for this light sensor board, and would like to ignore the larger ones.  Scroll to the right end of the filters and you'll find the "Size/Dimension" filters.  Select every option that is less than 2mm x 4mm, then click "Apply All" again.

<img src="/assets/lab2a/digikey-resistor-search4.png" style="border-radius: 1em">

At this point, all the remaining resistors match our electrical and physical requirements, so we can just pick the cheapest option, add it to cart, and call it a day.

For R3, you can use the same filters but with a resistance of 5.1 MΩ (note this is megaohms (MΩ), not milliohms (mΩ)).  Note that the same sizes may not be available for the 5.1 MΩ resistor, so pick something reasonable small (a cursory search suggests 2.3 x 6 mm, or at least below 2.5 x 6.5 mm).

## Capacitors
Searching for capacitors is very similar to searching for resistors.  First, limit your search to **Ceramic Capacitors**.

<img src="/assets/lab2a/digikey-capacitor-search1.png" style="border-radius: 1em">

Then, use the following filters, just as you did for the resistors:

| Mounting Type | Surface Mount, MLCC |
| Tolerance | ±10% |
| Temperature Coefficient | X5R |
| Package/Case | 0805 (2012 Metric) |
| Capacitance Value | *As noted in the schematic* |
| Part Status | Active |
| Stocking Option | In Stock |

## Remaining Components
Please find the rest of the components listed in the table above and add them to your Digikey cart.