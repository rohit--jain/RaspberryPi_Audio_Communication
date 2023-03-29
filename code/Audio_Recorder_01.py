import pyaudio
import wave
import sys
import os
from datetime import datetime
recordingStatusIndicator = "already_rec.txt"

def main():
    if len(sys.argv) > 1:
        if not os.path.exists(recordingStatusIndicator):
        # make sure only one instance is recording concurrently    
            f = open(recordingStatusIndicator, "w")
            f.close()

        # get USB mic interface number
            commandLineParameter = sys.argv[1]

        # setup pyaudio stream params
            form_1 = pyaudio.paInt16 # 16-bit resolution
            chans = 1 # 1 channel
            samp_rate = 44100 # 44.1kHz sampling rate
            chunk = 4096 # 2^12 samples for buffer
            record_secs = 5 # seconds to record
       
            dev_index = int(commandLineParameter)
            wav_output_filename = get_New_Recording_FileName() # name of .wav file

            audio = pyaudio.PyAudio() # create pyaudio instantiation

        # create pyaudio stream
            stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                            input_device_index = dev_index,input = True, \
                            frames_per_buffer=chunk)
            print("Recording into: " + wav_output_filename + " for " + str(record_secs) + " seconds...")
            frames = []

        # loop through stream and append audio chunks to frame array
            for ii in range(0,int((samp_rate/chunk)*record_secs)):
                data = stream.read(chunk)
                frames.append(data)

            print("Finished Recording")

        # stop the stream, close it, and terminate the pyaudio instantiation
            stream.stop_stream()
            stream.close()
            audio.terminate()

        # save the audio frames as .wav file
            wavefile = wave.open(wav_output_filename,'wb')
            wavefile.setnchannels(chans)
            wavefile.setsampwidth(audio.get_sample_size(form_1))
            wavefile.setframerate(samp_rate)
            wavefile.writeframes(b''.join(frames))
            wavefile.close()

        # remove currently recording status indicator
            os.remove(recordingStatusIndicator)
        else:
            print("Recording in progress...")
    else:
        print("Please provide the USB Mic Device Interface Number as Command Line Parameter")
        
def get_New_Recording_FileName():
    fileExt = '.wav'
    currentTime = datetime.now()
    currentHour = currentTime.hour
    currentMinute = currentTime.minute
    currentSecond = currentTime.second
    fileName = str(currentHour) + '_' + str(currentMinute) + '_' + str(currentSecond) + fileExt
    return fileName
    
if __name__ == "__main__": main()
