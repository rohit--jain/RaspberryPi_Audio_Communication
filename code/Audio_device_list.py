import pyaudio
audioInstances = pyaudio.PyAudio()
for deviceIndex in range(audioInstances.get_device_count()):
	print(audioInstances.get_device_info_by_index(deviceIndex).get('name'))
