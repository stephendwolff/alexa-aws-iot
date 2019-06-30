Alexa AWS IoT
=================

This small script sits and waits for incoming MQTT messages as an Amazon IoT MQTT client

Installation
-----------
Set up a python3 virtual environment:

`python3 -m venv venv`

Install the library

`pip install AWSIoTPythonSDK` or `pip install -r requirements.txt`

Configuration
--------
Set up public, private and certificate files for an Amazon IoT device, download and put in the certs directory.

See: 
 - https://docs.aws.amazon.com/iot/latest/developerguide/register-device.html
 
Also follow the instructions for setting up a coverall policy for the device.

Update device.py setting the file names for the public and private certificates, and also for the the device, see 'UPDATE THIS'.

*NB the device ID is in the default US-EAST-1 amazon region*, you may need to update this as well.

Use
---

Run with:

```.env
$ python3 device.py
```

this sits and waits for 