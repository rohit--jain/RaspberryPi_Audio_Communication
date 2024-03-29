### Prequisities:

[1] Install python3 pip package for sound meter. For details refer: https://github.com/shichao-an/soundmeter
You may need to install extra python packages along the way to complete this step.

[2] If soundmeter doesn't run directly from command line then do this step:

Add entry to PATH variable for '/home/pi/.local/bin'
To do this you need to sudo nano ~/.bashrc 
and add following lines at the end:

```
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```
For details refer following forum post: https://forums.raspberrypi.com/viewtopic.php?t=287068

[3] Reboot to apply changes. After reboot soundmeter should directly run from terminal

[4] Make sure your Sound Volume settings has appropiate selection for "AV Jack" or "HDMI"

[5] Make sure your USB microphone is connected to USB 2.0 port -> top slot and not bottom on the Raspberry Pi 4. Also make sure that microphone volume is set to maximum level for properly recording sound. 

[6] Make Recording_Activate.sh executable with following command:
```
chmod +x Recording_Activate.sh
```

### How to run recording script:

Once all python packages have been installed and soundmeter runs directly from command line, to activate recording use the following command:

```
soundmeter --trigger +70 --action exec --exec Recording_Activate.sh
```

### Please Note
[1] Trigger value +70 will change depending on noise level of your environment and sensitivity of your microphone. 
Start with a lower value and then gradually increment value to get personalized settings

[2] Recording_Activate.sh script has USB Microphone interface listed as 4. This maybe different on different raspberry pi and may change depending on USB Controller settings. To update to correct value check instructions for running Audio_Recoder.py from ([Audio_Recorder.md](https://github.com/rohit--jain/RaspberryPi_Audio_Communication/blob/main/code/Audio_Recoder.md))

[3] You can list connected Audio devices using script 
```python3 Audio_device_list.py```

[4] Before execution of script if the following file exists please DELETE it:
``` already_rec.txt ```
This file is a circumvent to make sure only one instance of Audio recording script runs concurrently
