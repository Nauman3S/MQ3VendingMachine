<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="artwork/mq3VM.png" alt="Project logo"></a>
</p>

<h3 align="center">MQ3 Vending Machine</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> MQ3 Vending Machine
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#deployment)
- [Installation and Config](#Installation_and_Config)
- [Test](#test)
- [Circuit](#circuit)
- [Smartphone App](#app)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This repo contains circuit, firmware and backend for MQ3 Vending Machine Project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites <a name = "Prerequisites"></a>

What things you need to install the software and how to install them.

```
- Raspberry Pi Model 3B, 3B+, 4B or CM4
```

## Installation and Configuration <a name = "Installation_and_Config"></a>

A step by step series that covers how to get the Firmware running.

### Raspberry Pi Firmware Pre-Reqs

1.  Download and install the latest Raspberry Pi OS Desktop image to your SD card
2.  Open the terminal and execute the following command
    ```sudo raspi-config```
3. Then follow the following pictures to enable I2C bus on you raspberry pi

* ![R1](artwork/r1.png)
* ![R2](artwork/r2.png)
* ![R3](artwork/r3.png)
* ![R4](artwork/r4.png)
* ![R5](artwork/r5.png)

* Then do the same for Serial(UART)

* ![R2](artwork/r2_2.jpg)

### Configuring Raspberry Pi and Running the UI
  1.  Copy Firmware folder to the desktop of your Raspberry Pi, open the terminal of your Raspberry Pi and execute the following commands

  - ```sudo apt-get update```
  - ```sudo apt-get upgrade```
  - ```sudo apt install python3-pip```
  - ```sudo pip3 install gas-detection```
  - ```cd ~/Desktop/Firmware```
  - ```sudo chmod a+rx starter.sh```


1.  To run the program just double click on starter.sh file
  1.  or execute `python3 /home/pi/Desktop/Firmware/Firmware.py`


## ⛏️ Testing <a name = "test"></a>

1.  The Firmware can be tested on Raspberry Pi 3B, 3B+ or 4B with the following modifications
  1.  Connect the sensor as shown in the Circuit Diagram section below.

## 🔌 Circuit Diagram <a name = "circuit"></a>


* RPi 3,4 GPIOs Pinout

![GPIOsRPi](Circuit/rpi34.jpg)

### Circuit

```http
Pins connections
```

| MQ3 | Logic Level Shifter |
| :--- | :--- |
| `A0` | `TX0` | 
| `GND` | `GND` | 
| `VCC` | `5V` | 

| Logic Level Shifter | ADS1115 |
| :--- | :--- |
| `TX1` | `A0` | 
| `GND` | `GND` | 
| `LV` | `3.3V` | 
| `HV` | `5V` | 


| ADS1115 | Raspberry Pi |
| :--- | :--- |
| `SCL` | `GPIO2` | 
| `SDA` | `GPIO3` | 
| `VCC` | `3.3V` | 
| `GND` | `GND` | 


![GPIOsRPiCkt](Circuit/Circuit.png)


## Components Used

1.  Any Raspberry Pi (https://www.amazon.com/CanaKit-Raspberry-Micro-Supply-Listed/dp/B01C6FFNY4/ref=sr_1_1?dchild=1&keywords=raspberry+pi+3&qid=1632029848&sr=8-1)
2.  MQ3 Sensor(https://www.amazon.com/ACROBOTIC-Alcohol-Breakout-Raspberry-Breathalyzer/dp/B07CSNGS87/ref=sr_1_5?dchild=1&keywords=mq3&qid=1632029867&sr=8-5)
3.  ADS1115(https://www.amazon.com/ADS1115-16-Bit-ADC-Programmable-Amplifier/dp/B00QIW4MGW/ref=sr_1_3?dchild=1&keywords=ads1115&qid=1632029889&sr=8-3)
4.  Logic Level Converter(https://www.amazon.com/SparkFun-Logic-Level-Converter-Bi-Directional/dp/B01N30ZCW9/ref=sr_1_6?crid=2NOGIA43AG9OS&dchild=1&keywords=logic+level+converter&qid=1632029917&sprefix=logic+level%2Caps%2C463&sr=8-6)


## ⛏️ Built Using <a name = "built_using"></a>

- [Python3](https://www.python.org/) - Raspberry Pi FW
- [Flutter](https://flutter.dev/) - Cross-Platform Smartphone App Development Framework

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
