Usage parameters:

```python3 Audio_Recorder_01.py <USB_MIC_INTERFACE_NUMBER>```

USB_MIC_INTERFACE_NUMBER can be found by running program with different numbers like 1,2,3,4,... to find the exact value. For example, in my system the following worked:

```python3 Audio_Recorder_01.py 4```

Recording is saved as .WAV file with name timestamp of the start time of recording 

To change the number of seconds of recording change number value of variable ```record_secs```
