### Prequisities:

[1] Install python3 pip package for sound meter. For details refer: https://github.com/shichao-an/soundmeter
You may need to install extra python packages along the way to complete this step.

[2] Add entry to PATH variable for '/home/pi/.local/bin'
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

[4] Make Recording_Activate.sh executable with following command:
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

[2] Recording_Activate.sh script has USB Microphone interface listed as 4. This maybe different on different raspberry pi and may change depending on USB Controller settings. To update to correct value check instructions in Audio_Recorder.md
