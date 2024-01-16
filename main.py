# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:04:52 2024

@author: hibad
"""

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt 

lambda_ = 44100
T = 0.1
duration=int(T*lambda_)

max_freq=2000


length=duration*2
freq = lambda_/length* np.arange(0, length)
length_max=int(max_freq*length/lambda_)
freq = lambda_/length* np.arange(0, length_max)
data=np.zeros(length)
while True:
    datum = sd.rec(duration, lambda_ , channels=1)
    sd.wait()
    datum=datum.flatten()
    data=np.concatenate((data, datum))
    data=data[-length:]
    f=np.fft.fft(data)
    PSD = (np.real(f*np.conjugate(f)/length))[0:length_max]
    print(freq[np.argmax(PSD)])
# data=np.fft.ifft(f)
plt.plot(freq, PSD)
# sd.play(data)

