import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sys
import string
import os
import scipy.signal as sig

def preprocess( pitch ):

	# trim zeros
	pitch = np.trim_zeros(pitch)

	#median filtering
	pitch = sig.medfilt(pitch, kernel_size=9)

	#interpolate code
	print pitch.size
	print len(np.arange(0,pitch.size))
	f2 = interp1d(np.arange(0,pitch.size), pitch, kind='cubic')
	xnew = np.linspace(0, pitch.shape[0]-1, 20)

	#plt.plot(xnew, f2(xnew), 'o')
	#plt.show()

	return f2(xnew)