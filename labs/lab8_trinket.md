---
layout: page
title: Trinket Lab
nav_exclude: true
description: Trinket Lab
permalink: /labs/lab8
---

Trinket Lab
==============

* Do not remove this line (it will not be displayed)
{:toc}



<div class="hero hero-mini">
<h1>HOPE: Trinket Lab</h1>
</div>
<article>
<!--kg-card-begin: html--><div><!--kg-card-end: html--><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div><!--kg-card-end: html--><!--kg-card-begin: markdown--><h1 id="introduction">Introduction</h1>
<p>This lab will go through how to program an ESP32-S2 with the Arduino environment and perform common project debugging procedures. You'll learn how to use the oscilloscope to look at and understand PWM and I2C signals.</p>
<!--kg-card-end: markdown--><figure class="kg-card kg-image-card"><img src="../assets/lab8/trinket.png" class="kg-image" alt="" loading="lazy" width="757" height="749"></figure><!--kg-card-begin: markdown--><h1 id="before-or-during-lecture">Before or During Lecture</h1>
<ol>
<li>Install the Arduino IDE: <a href="https://www.arduino.cc/en/software?ref=ieee.berkeley.edu">https://www.arduino.cc/en/software</a></li>
<li>Launch and navigate to the File &gt; Preferences Window</li>
<li>Under “Additional Board Manager URLs” add the following link <a href="https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json?ref=ieee.berkeley.edu">https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json</a> to the textbox.</li>
<li>Go to Tools &gt; Board &gt; Boards Manager and search up esp32 in the top. Install the esp32 package by Espressif Systems</li>
<li>We’ll be using a pre-written library to communicate with the temperature sensor.<br>
a. To install it, navigate to Sketch &gt; Include Library &gt; Manage Libraries<br>
b. Search up <strong>PCT2075</strong> and install the Adafruit library. Do the same for the <strong>BusIO</strong> library. If you get a message along the lines of "The library (name) needs some other dependancies...", click "Install all"</li>
</ol>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="programming-and-general-reference">Programming and General Reference</h1>
<h2 id="scope-setup">Scope setup</h2>
<p>Turn your scope on. The power button may require a strong press.</p>
<p>Make sure that all channels are set to DC coupling! AC coupling means all DC voltages will be ignored (same as adding a capacitor in series with the sense line) and will be useless for this lab. Press the channel button (e.g. "1") to open the relevant menu.</p>
<img src="../assets/lab8/trinket4.png" alt="oscope" width="50%/">
<p>Make sure you are using oscilloscope probes (grey), not the signal generator leads (black, with two alligator clips). You may need to gently remove the probe cap to reach some signals. <strong>Please re-attach the probe cap when done--they can cost up to $100 to replace!</strong></p>
<img src="../assets/lab8/trinket7.jpeg" alt="oscope" width="50%/">
<h2 id="trinket-schematic">Trinket schematic</h2>
<p>Below is part of the schematic showing which pins are connected to what on the trinket. The bottom two pins are SDA (top) and SCL (bottom) for the I2C:</p>
<img src="../assets/lab8/trinket_sch.png" alt="trinket schematic" width="50%/">
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-0-downloading-starter-code-and-programming">Part 0: Downloading Starter Code and Programming</h1>
<p>Download our starter Arduino code here: <a href="https://gist.github.com/rgovindjee/4d0c31d0e8dcb66c9798764f958552e0?ref=ieee.berkeley.edu">https://gist.github.com/rgovindjee/4d0c31d0e8dcb66c9798764f958552e0</a></p>
<p>First, we recommend you display line numbers:<br>
<img src="../assets/lab8/line_numbers.png" alt="change code" width="50%/"></p>
<p>The next thing you should do is change these lines appropriately:<br>
<img src="../assets/lab8/modify_code.png" alt="change code" width="80%/"></p>
<p><strong>The password must be greater than or equal to 8 characters long.</strong></p>
<h2 id="arduino-ide-setup">Arduino IDE Setup</h2>
<p>Before flashing and programming:</p>
<ul>
<li>Under Tools &gt; Board, choose <strong>ESP32S2 Dev Module</strong></li>
<li>make sure <strong>USB CDC on Boot is set to "Enabled"</strong></li>
<li>upload mode is <strong>Internal USB</strong></li>
</ul>
<p>All settings should match the image below.</p>
<p><img src="../assets/lab8/trinket2.png" alt="trinket2" loading="lazy"></p>
<h2 id="first-time-programming-instructions">First-time programming instructions</h2>
<ol>
<li>Press and <strong>hold down</strong> the BOOT button on the trinket.</li>
<li>While holding down boot, press and <strong>release</strong> the RESET button.</li>
<li>Release the BOOT button.</li>
</ol>
<p>Choose the right port under Tools &gt; Port.</p>
<p>On Windows, this may require opening Device Manager to check which COM port your board is available on (You are looking for a "USB Serial" device):</p>
<p><img src="../assets/lab8/trinket3.png" alt="trinket3" loading="lazy"></p>
<p>or on MacOS:</p>
<ol>
<li>Open terminal and type: ls /dev/*.</li>
<li>Note the port number listed for /dev/tty.usbmodem* or /dev/tty.usbserial*. The port number is represented with * here.</li>
</ol>
<p>Click on the upload button (the right pointing arrow in the toolbar)<br>
<img src="../assets/lab8/image.png" alt="programming-image" loading="lazy"></p>
<p>and the status console at the bottom should eventually show some text about data being written to the ESP32.</p>
<p><img src="../assets/lab8/trinket1.png" alt="trinket1" loading="lazy"></p>
<p>You <strong>should</strong> get an error asking you to reset the board.<br>
Press and release the RESET button. Your code should now be running.</p>
<p>NOTE: Mac users, if you get an error with Arduino not finding python in $PATH, try the following command in terminal:</p>
<ul>
<li><code>sed -i -e 's/=python /=python3 /g' ~/Library/Arduino15/packages/esp32/hardware/esp32/*/platform.txt</code></li>
</ul>
<h2 id="programming-instructions-after-the-first-time">Programming instructions after the first time</h2>
<p>Check that the correct port is selected in the Tools &gt; Port menu. <em>It may change after first-time programming</em>.</p>
<p>You should be able to upload new firmware with the Upload button without having to physically press any buttons on the trinket board (they are controlled automatically by the ESP32-S2). If this is not the case, check that your settings are current under Tools (see above) and repeat first-time programming.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-1-blinking-and-fading-leds-with-pwm">Part 1: Blinking and Fading LEDs with PWM</h1>
<p>There’s a RGB LED in the middle of the board. We’ve pre-defined the pins in the starter code (blue on pin 10, red on pin 11, green on pin 12).</p>
<p>We’ve written some code to cycle the LED through a rainbow.<br>
<strong>Uncomment the block of code labeled Part 1 in the loop function</strong> and for the later parts of the lab uncomment their respective blocks.</p>
<p>The brightness is controlled by PWM’ing each color channel. In code this is done with the analogWrite function, which takes in the pin you want to write to and a value from 0 to 255 for the duty cycle. Upload the code and then use the oscilloscope to probe the R, G, and B channels. We’ve exposed the signals to pads along the edge for easy probing.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h3 id="pwm-testing">PWM Testing</h3>
<p>First, what is PWM? PWM stands for <strong>P</strong>ulse <strong>W</strong>idth <strong>M</strong>odulation, and is a way to <em>approximate</em> an analog voltage with a purely digital signal. Digital signals only have 2 discrete states: HIGH and LOW (on and off, 1 and 0, etc.). However, if you flip between the HIGH and LOW states fast enough, the <em>average</em> output voltage over a period of time then resembles some continuous value inbetween the HIGH and LOW voltages. Subsequently, we can change this perceived average continuous value by changing the <strong>duty cycle</strong> of the HIGH-LOW oscillation. The duty cycle is the % of time in a period that the output is HIGH.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="../assets/lab8/Duty_Cycle_Examples.png" alt="duty cycle example" style="width: 60%; margin: auto; display:block"> <br><!--kg-card-end: html--><!--kg-card-begin: markdown--><p>Using the scope to see the PWM signal:</p>
<ul>
<li>Set horizontal scale to <strong>1 ms/division</strong></li>
<li>Set vertical scale to <strong>2 V/div</strong></li>
<li>Connect probe GND to GND</li>
<li>Touch probe tip to any of the RGB pads along the edge.</li>
<li>Set trigger to <strong>Edge</strong> mode, on the channel that you're using (typ. <strong>channel 1</strong>), and to trigger on either only falling or <strong>only rising edges</strong> (not both).</li>
<li>Set the trigger to <strong>~1.8V</strong> using the knob under the Trigger controls (this should cause the waveform to align on your screen around a single edge)</li>
</ul>
<p>Depending on the last person to use the scope, you <strong>may</strong> have to lower the holdoff time (lockout before re-trigger) to get the waveform to display smoothly.</p>
<p>Go to the trigger settings by pressing "Mode":</p>
<img src="../assets/lab8/trinket5.png" alt="oscope2" width="50%/">
<p>And adjust as low as 90ns using the knob with the ⟲ light next to it.</p>
<p><strong>This primarily applies to the older (gray) scopes, but may be needed on newer (black) scopes as well.</strong></p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h3 id="checkoff-requirements">Checkoff requirements</h3>
<p><strong>Checkoff task: Take a picture with your phone of one of the channels.</strong></p>
<p><strong>Checkoff question: Along with the picture of the PWM waveform, what’s the PWM frequency?</strong> You can choose to count divisions, use the cursors, or use the Measure functions in the oscilloscope.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-2-capacitive-touch-sensors">Part 2: Capacitive Touch Sensors</h1>
<p>On the left and right of the board are capacitive touch sensors: a slider on the left and three individual buttons on the right. When you put your finger on the pads, your body changes the capacitance on the node and the microcontroller can detect this change with some clever timing of discharge time of an RC circuit.</p>
<p><strong>Uncomment the block of code labeled Part 2 in the loop function</strong>.<br>
You may leave Part 1 running.</p>
<p>The starter code prints out the reading from the touch pads. To see the values, go to Tools &gt; Serial Monitor. Make sure the baud rate in the bottom right is 115200.</p>
<p>The capacitive touch <em>may</em> work better if you lift the trinket off the mat/table.</p>
<p><strong>Checkoff task: Write some code that changes the LED based on if your finger is on a pad.</strong></p>
<p><em>Hint (Optional):</em> You may get better results if you set a threshold for the <em>rate of change</em> of capacitive touch values instead of threshold for a raw capacitance value. This is not requried to get checked off, though.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-3-analog-light-sensor">Part 3: Analog Light Sensor</h1>
<p>We have a BH1603 ambient light sensor (ALS) on the board with an analog output.</p>
<p>We can read analog input pins with analogRead, which outputs a value from 0 to 4095 that is roughly proportional to 0 to 2.5V (when using the ADC in the most common mode).</p>
<p><strong>Uncomment the block of code labeled Part 3 in the loop function</strong>.<br>
You may leave Part 2 running.</p>
<p><strong>Checkoff task: Use the oscilloscope or multimeter to probe the output of the sensor and see how it changes under different lighting conditions. Does the voltage go up or down when more light is available?</strong></p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-4-temperature-sensor-and-i2c">Part 4: Temperature Sensor and I2C</h1>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><p>We have a PCT2075 temperature sensor on the board that is connected to the ESP32 by I2C. If you haven’t already done so, install the required libraries to communicate with the sensor by following the instructions in the prelab.</p>
<p>The default code will print out the temperature from the sensor.</p>
<p><strong>Uncomment the block of code labeled Part 4 in the loop function</strong>.<br>
You may leave Part 3 running.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h3 id="i2c">I2C</h3>
<p>I2C is a two wire serial communication protocol (also called two wire interface, or TWI) that is commonly used to interface microcontrollers, sensors, and other embedded hardware. One wire is used for the clock (SCL), which tells the devices when to read the data bits. The other wire is the data line (SDA) and carries data to and from devices.</p>
<p>Every device on the bus has an address, and up to 127 different devices can be on one set of two wires assuming they all have unique addresses. A good reference on this can be found on <a href="https://www.analog.com/en/technical-articles/i2c-primer-what-is-i2c-part-1.html?ref=ieee.berkeley.edu">Analog Device's website</a>.</p>
<p>All data packets going from the microcontroller to the device that we want to talk to on the bus are prefixed with the address of the device. All the devices on the bus listen to this address and if it matches their internal address, they will reply while the rest remain silent.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: html--><br><img src="../assets/lab8/i2c_timing.png" alt="I2C timing diagram" style="width: 60%; margin: auto; display:block"> <br>

<!--kg-card-end: html--><!--kg-card-begin: markdown--><p>Use the oscilloscope with two probes and probe the SDA and SCL lines of the I2C bus. Capture the transmission of a single packet of data (use single triggering on the SDA lines). The address of the temperature sensor is the first byte of any transmission. Can you decode the data and read out the address? The data line is sampled while the clock is <strong>high</strong>, and the address is <strong>7 bits</strong>.</p>
<h3 id="scope-setup-mostly-for-grey-oscilloscopes">Scope Setup (mostly for grey oscilloscopes)</h3>
<p>If you are using one of the newer (black) oscilloscopes, this may section <em>may</em> apply. Only follow these instructions if you are unable to capture the waveform using the "How to use Single Trigger instructions below".</p>
<p>For older scopes, you will have to adjust the "holdoff" time--this causes the scopes not to immediately force a capture after no trigger edge is detected in one window.</p>
<p>Go to the trigger settings by pressing "Mode":</p>
<img src="../assets/lab8/trinket5.png" alt="oscope2" width="50%/">
<p>And adjust to 1-2s</p>
<img src="../assets/lab8/trinket6.png" alt="oscope3" width="50%/">
<h3 id="how-to-use-single-trigger">How to use Single Trigger</h3>
<p>You may have to remove the hook attachment on one or both probes to physically be able to probe these signals. <strong>MAKE SURE BOTH GROUND CLIPS ARE CONNECTED TO A BOARD GND!</strong></p>
<ol>
<li>Probe both the SDA and SCL lines and turn on both of the channels your probes are on (press the button "2" to enable Channel 2).</li>
<li>Set the trigger level to 1.8 V (trigger menu); you can set the trigger to either channel.</li>
<li>Set the horizontal scale to 20 us/div</li>
<li>Set the vertical scale to 1 V/div</li>
<li>Set the vertical offset to 2V (this centers the waveform so we can see all of it)</li>
<li>Arm the trigger by pressing the Single button. This may immediately cause a capture on the scopes we have in lab (this is not typical for scopes in general!), so you’ll need to press it again to capture the signal of interest.</li>
<li>You should now see some data and clock waveforms since we are reading the sensor periodically.</li>
</ol>
<p>When the bus is not in use, both SDA and SCL will be pulled high (with pull-up resistors).</p>
<p><strong>Checkoff task: Take a picture of the start of the packet and decode the device address using the diagram above. <a href="https://www.rapidtables.com/convert/number/binary-to-hex.html?ref=ieee.berkeley.edu">Convert the binary address to hex</a>. Note that many data bytes can be read/written after the device address.</strong></p>
<p><strong>Checkoff task: Zoom in to 200ns/div horizontal resolution and capture an image of a falling edge on either SDA or SCL. What do you notice about the waveform? Why doesn't this happen on the rising edge?</strong></p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="part-5-wifi">Part 5: Wifi</h1>
<p><strong>Uncomment the block of code labeled Part 5 in the loop function</strong>.<br>
You may leave Part 4 running.</p>
<p>Upload your code to the trinket. In the Arduino Serial Monitor, note down the IP address being printed by your trinket.</p>
<p>Using your laptop, connect to the newly avaliable WiFi network (that should be your name if you followed Step 0!), using the password you set (which should be at minimum 8 characters long).</p>
<p>Verify that you have successfully connected. (NOTE: You may get a warning that the WiFi network is not connected to the internet, this is OK - ignore the warning and make sure you are connected regardless).</p>
<p>On your laptop, open the terminal or powershell or cmd prompt, and ping the IP address of your trinket by using:</p>
<ul>
<li><code>ping IP_ADDRESS_HERE</code></li>
</ul>
<p>(replace IP_ADDRESS_HERE with your trinket's IP).</p>
<p><strong>Checkoff task: Take a screenshot of your terminal/powershell/cmd window showing the successful ping.</strong></p>
<p>(Optional): In your project, you may want to communicate sensor data over WiFi. For the trinket, you can imagine communicating the temperature readings over WiFi. To do this, we often use a common IoT protocol called MQTT. Learn more about it here: <a href="https://learn.adafruit.com/adafruit-io/mqtt-api?ref=ieee.berkeley.edu">https://learn.adafruit.com/adafruit-io/mqtt-api</a></p>
<p>(Optional): Try connecting to your neighbor's WiFi networks with the default password 'password' and shame them if they haven't changed it according to instructions.</p>
<!--kg-card-end: markdown--><!--kg-card-begin: markdown--><h1 id="checkoff-requirements">Checkoff Requirements</h1>
<ul>
<li>PWM picture and PWM frequency</li>
<li>Capacitive touch causing some visible change on the board</li>
<li>Probe the light sensor output to see changes in voltage</li>
<li>I2C scope picture and decoded address</li>
<li>I2C falling edge picture and answer to "what is different about the falling and rising edges?"</li>
<li>Picture of successful ping</li>
</ul>
<!--kg-card-end: markdown--><!--kg-card-begin: html-->      <div class="linkbox">
<div class="newh2"><a href="https://ieee.berkeley.edu/hope/" style="font-weight: 700;">HOPE Main Page</a></div>
</div><!--kg-card-end: html--><!--kg-card-begin: html--></div><!--kg-card-end: html-->
</article>