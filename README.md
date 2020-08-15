
![GUI](/images/Gui.png)


 Control RPi with GUI 
===========

This repository contains code necessary to use a Raspberry Pi to make GUI app with sensors monitor with various functions such as control actuators, Graph sensors output,
email to gmail and alarm.  This code can work on any Raspberry Pi. It works on Raspberry pi 3 Model B.

Currently, the software display the sensors states and take the data from GUI and a sensors and enables you to control the following:
- Fan (on, off, speed)
- Led (intensity)
- Relay module (open switch or close switch)
- Servo (rotation angle)

Pin connections
---------------

Currently the pins of the Raspberry Pi are connected in the following way:


![circuit connections on fritzing](/images/circuit-connection.png)


Prerequisites:
-----------------

In order to run program, you need to have the following installed:

- Python 3
- guizero https://github.com/lawsie/guizero
- pygame https://github.com/pygame/pygame

Getting Started
------------------

> Now clone and run the program on your raspberry pi

```
$ git clone https://github.com/hosniadel666/RPi-Control-GUI.git

$ cd ..../src

$ sudo python3 Gui.py
```
