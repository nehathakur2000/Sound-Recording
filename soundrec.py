import sounddevice

from scipy.io.wavfile import write

def record_audio(second,file):
    print("start recording...")
    voice=sounddevice.rec((second*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write(file,44100,voice)
record_audio(10,"ok.wav")
print("done")
