### Prequisities:

[1] Install python3 pip package for sound meter. For details refer: https://github.com/shichao-an/soundmeter

[2] Add entry to PATH variable for '/home/pi/.local/bin'
To do this you need to sudo nano ~/.bashrc 
and add following lines at the end:

'''
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
'''
For details refer following forum post: https://forums.raspberrypi.com/viewtopic.php?t=287068

