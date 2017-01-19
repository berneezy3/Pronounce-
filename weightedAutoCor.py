import scipy.io.wavfile as wf 
import scipy.signal as sig
import numpy as np
np.set_printoptions(threshold=np.nan)
import sys
import pyaudio



def multiplySignals(x, y):
	sum = 0
	for i in (0,len(x)):
		sum = sum + x(i) * y(i)
	return sum

#AUTOCORRELATION FUNCTION
#(1/N)Sigma{n=0, N-1}(x(n), x(x+m))
#take in signal
def pitchByACF(wavFile, mmin=50, mmax=260, N=1024):
	rate = wavFile[0]
	soundArr = np.mean(wavFile[1], axis=1)
	#print type(soundArr)
	# convert mmin and mmax from hertz to samples
	tempMin = mmin
	tempMax = mmax
	mmin = int((1./tempMax) * rate)
	mmax = int((1./tempMin) * rate)
	#print mmin, mmax


	# amount of windows that can be fit into the audio file
	# can also be seen as the starting points of window
	numPitchPts = (len(soundArr) - mmax)/N
	pitchArr = np.zeros(numPitchPts)
	for i in range(0,numPitchPts):
		window = soundArr[i*N:(i+1)*N]
		maxDm = float('-inf')
		pitchPt = 0

		

		for m in range(mmin, mmax):
			slidedWindow = soundArr[i*N+m:(i+1)*N+m]
			AC = np.sum( np.multiply(window, slidedWindow)) / N
			#print Dm
			if AC > maxDm:
				#print AC
				maxDm = AC
				# convert pitch from samples back to hertz
				#if AC > 300000:
				pitchPt = m
				#else:
				#	pitchPt = 0.1

		pitchArr[i] = 1/(float(pitchPt)/rate)
		# print pitchPt

	return pitchArr


# AMDF (Average Magnitude Difference Function)
# D(m) = 1/N Sigma{n=0 -> N-1}( abs( x(n) - x(n+m) ) )
# N = window size
# pitch = MIN(D(m)), for m= mmin to mmax (range of expected pitches)
# mmin and mmax in hertz
def pitchByAMDF(wavFile, mmin=50, mmax=260, N=1024):
	rate = wavFile[0]
	soundArr = np.mean(wavFile[1], axis=1)
	#print type(soundArr)
	# convert mmin and mmax from hertz to samples
	tempMin = mmin
	tempMax = mmax
	mmin = int((1./tempMax) * rate)
	mmax = int((1./tempMin) * rate)
	#print mmin, mmax


	# amount of windows that can be fit into the audio file
	# can also be seen as the starting points of window
	numPitchPts = (len(soundArr) - mmax)/N
	pitchArr = np.zeros(numPitchPts)
	for i in range(0,numPitchPts):
		window = soundArr[i*N:(i+1)*N]
		minDm = sys.maxint
		pitchPt = 0

		#print "window #", i, "\n"

		for m in range(mmin, mmax):
			slidedWindow = soundArr[i*N+m:(i+1)*N+m]
			AMD = np.sum( (np.absolute(window - slidedWindow)) ) / N

			if AMD < minDm:
				#print AMD
				minDm = AMD
				# convert pitch from samples back to hertz
				if AMD > 150:
					pitchArr[i] = 1/(float(m)/rate)
				else:
					pitchPt = None

		
		# print pitchPt

	return pitchArr


# WEIGHTED AUTOCORRELATION FUNCTION
def pitchByWACF(wavFile, mmin=50, mmax=260, N=1024):
	#print np.mean(wavFile[1], axis=1)
	rate = wavFile[0]
	print rate
	soundArr = wavFile[1]
	soundArr = soundArr.astype(np.float64)
	print soundArr.size
	#print "from WAC, soundArr: "
	#print type(soundArr)
	# convert mmin and mmax from hertz to samples
	tempMin = mmin
	tempMax = mmax
	mmin = int((1./tempMax) * rate)
	mmax = int((1./tempMin) * rate)
	#print mmin, mmax


	# amount of windows that can be fit into the audio file
	# can also be seen as the starting points of window
	numPitchPts = (len(soundArr) - mmax)/N

	pitchArr = np.zeros(numPitchPts)
	for i in range(0,numPitchPts):

		window = soundArr[i*N:(i+1)*N]
		maxDm = float('-inf')
		pitchPt = 0

		#print "window #", i, "\n"

		for m in range(mmin, mmax):

			slidedWindow = soundArr[i*N+m:(i+1)*N+m]
			AC = np.sum( np.multiply(window, slidedWindow)) / N
			AMD = np.sum( (np.absolute(window - slidedWindow)) ) / N
			WAC = AC/(AMD+1)
			#print maxDm
			if WAC > maxDm:
				maxDm = WAC
				#print WAC
				# convert pitch from samples back to hertz
				if WAC > 1500:
					#print WAC
					pitchArr[i] = 1/(float(m)/rate)
				else:
					pitchPt = None


	return pitchArr


