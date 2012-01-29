#!/usr/bin/env python
# coding: -*- utf8 -*-
# save a wav file in python via numpy/scipy
# author: harald schilly <harald@schil.ly>
# license: bsd
# depends on numpy, scipy and matplotlib
# inspiration: http://lac.linuxaudio.org/2011/papers/40.pdf
# and http://glowingpython.blogspot.com/2011_09_01_archive.html

import numpy as np
from scipy.io import wavfile

# seconds
duration = 5
# 8000 is nice for the spectral plot, go up to 44100 if you like
rate = 8000
# samples in 16bit wav are -2^15 to +2^15
# assumption is, that the functions are normalized between
# -1 and +1 before conversion to int16
amplify = 2**15 

x = np.linspace(0, 2 * np.pi * duration, duration * rate)
# the function in y should be in the range -1 to +1
# samples will be int16, from -2^15 to +2^15
sound1 = amplify * np.sin(440 * x)# * np.cos(x)

# note the astype(np.int16)
wavfile.write('npsound.wav', rate, sound1.astype(np.int16))

### second example
x = np.linspace(0, duration, duration * rate)
sound2 = amplify * np.sin(2*np.pi* (440 + 220 * x/duration) * x) * np.cos(2*np.pi*x*220)

wavfile.write('npsound2.wav', rate, sound2.astype(np.int16))

# spectral plot
from pylab import plot, show, subplot, specgram
subplot(211)
plot(x, sound2)
subplot(212)
specgram(sound2, NFFT=256, noverlap=0)
show()
