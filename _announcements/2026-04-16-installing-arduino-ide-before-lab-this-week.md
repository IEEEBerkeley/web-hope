---
title: "Installing Arduino IDE Before Lab this Week"
date: 2026-04-16
author: "Roman Silivra"
category: "Project"
type: "announcement"
---

Hello everybody, 

Sorry for the short notice, but please check out this post to be more prepared for lab section this week!

Before coming to lab this week (if possible), please follow the instructions below to download and install the Arduino IDE and the libraries we will use for the lab. The internet in Cory is flaky and you may have a hard time doing this in lab. Also if you have one, bring a USB-C cable to lab that you can use with your computer.

Install the Arduino IDE: https://www.arduino.cc/en/software

Launch and navigate to the File > Preferences Window

Under “Additional Board Manager URLs” add https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json to the textbox.

Go to Tools > Board > Boards Manager and search up esp32 in the top. Install the esp32 package by Espressif Systems

We’ll be using a pre-written library to communicate with the temperature sensor.

To install it, navigate to Sketch > Include Library > Manage Libraries

Search up PCT2075 and install the Adafruit library. Do the same for the BusIO library. If you get a message along the lines of "The library (name) needs some other dependencies....", click "Install all"

All the best,

HOPE Staff
