import scipy.io.wavfile as wf 
import numpy as np
import sys
import pyaudio
import math
import matplotlib.pyplot as plt

from weightedAutoCor import *
from preprocess import *

soundFile = sys.argv[1]
dataArr = wf.read(soundFile)
rate = dataArr[0]
soundArr = dataArr[1]

soundFile2 = sys.argv[2]
dataArr2 = wf.read(soundFile2)
rate2 = dataArr2[0]
soundArr2 = dataArr[1]

WACFpitchArr2 = pitchByWACF(dataArr2)
WACFpitchArr2 = preprocess(WACFpitchArr2)

ACFpitchArr = pitchByACF(dataArr)
AMDFpitchArr = pitchByAMDF(dataArr)
WACFpitchArr = pitchByWACF(dataArr)
WACFpitchArr = preprocess(WACFpitchArr)
print WACFpitchArr

np.savetxt('AMDFpitchArray', AMDFpitchArr)
np.savetxt('ACFpitchArray', ACFpitchArr)
np.savetxt('WACFpitchArray', WACFpitchArr)

time=np.arange(0,len(WACFpitchArr),1);
time2=np.arange(0,len(AMDFpitchArr),1);

time3=np.arange(0,len(WACFpitchArr2),1);


#pitch contour plot
f = plt.figure(1)
plt.subplot(211)
plt.scatter(time, WACFpitchArr, color='green')
plt.scatter(time3, WACFpitchArr2, color='red')
plt.xlabel('time (s)')
plt.yscale('log')
plt.ylabel('frequency(Hz)')
plt.ylim([0,500])
plt.xlim([0,140])
plt.title('tone of ma(1st) vs. tone of ma(2nd)')
plt.grid(True)
plt.subplot(212)
plt.plot(soundArr)
plt.yscale('log')

plt.show()

'''
g = plt.figure(2)
plt.subplot(211)
plt.scatter(time2,AMDFpitchArr)
plt.xlabel('time (s)')
plt.ylabel('frequency(Hz)')
plt.ylim([0,500])
plt.title('pitch contour')
plt.grid(True)
plt.subplot(212)
plt.plot(soundArr)
#g.show()
'''

