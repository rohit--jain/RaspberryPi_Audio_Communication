# RaspberryPi_Audio_Communication

USB Mic Audio Processing -> Noise level detection + Recording using Raspberry Pi

check markup descrption files inside [code](https://github.com/rohit--jain/RaspberryPi_Audio_Communication/tree/main/code) folder for detailed setup and run instructions

# Description 

This python project records Audio from USB Mic for specified [number of seconds] when ambient noise of certain [RMS threshold value] (Volume) is observed.

To engage noise based trigger I used shichao-an's ([soundmeter](https://github.com/shichao-an/soundmeter)) project, which provides soundmeter as a PIP package

Upon trigger I execute python script for audio recording through a shell script

Recording is saved in WAV audio format with file name of current time stamp 

There is a special check to ensure only one file gets recorded concurrently while receiving multiple triggers.

# To Do:
Provide functionality to upload files to a local FTP server over LTE 
