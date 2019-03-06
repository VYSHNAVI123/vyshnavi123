import scipy.io.wavfile as wav
import numpy as a
import matplotlib.pyplot as plt
fs,data=wav.read('vyshu.wav')
print(fs,len(data),data)
plt.subplot(2,2,1)
plt.plot(data)
t=a.arange(0,len(data)/fs,1.0/fs)
plt.plot(t,data)
plt.show()
wav.write('voice-slow.wav',0.2*fs,data)

