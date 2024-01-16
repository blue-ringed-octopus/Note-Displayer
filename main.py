# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:04:52 2024

@author: hibad
"""

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt 
import cv2

def closest_note(freq, notes):
    i=np.argmin(np.abs(freq-np.asarray(list(notes.values()))))
    return list(notes.keys())[i]

note_names=["A4","AS4","B4", "C5", "CS5", "D5", "DS5","E5", "F5", "FS5","G5", "GS5",
            "A5","AS5","B5", "C6", "CS6", "D6", "DS6","E6", "F6", "FS6","G6", "GS6",  
            "A6","AS6","B6", "C7", "CS7", "D7", "DS7","E7", "F7", "FS7","G7", "GS7", ]
notes={}

note_names_low=["A3","AS3","B3", "C4", "CS4", "D4", "DS4","E4", "F4", "FS4","G4", "GS4", "A4"]

for i, note in enumerate(note_names_low):
    notes[note]=440*2**((i-len(note_names_low)+1)/12)
    
for i, note in enumerate(note_names):
    notes[note]=440*2**(i/12)



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
    dom_freq=freq[np.argmax(PSD)]
    print(closest_note(dom_freq,notes ))
# data=np.fft.ifft(f)
plt.plot(freq, PSD)
# sd.play(data)

