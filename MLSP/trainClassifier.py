# Scikit learn SVM
from sklearn.svm import SVC
import numpy as np
import glob
import pickle
import cPickle
from sklearn.externals import joblib
import scipy.io.wavfile as wf 
import matplotlib.pyplot as plt
from weightedAutoCor import *
from preprocess import *
'''
Collect all wav files
'''
m0t1wav  = []
m1t1wav  = []
m0t2wav  = []
m1t2wav  = []

'''
Variables to store pitches/Label Matrices for training data
'''
m0t1pitch  = []
m1t1pitch  = []
m0t2pitch  = []
m1t2pitch  = []


'''
Label Vector
'''
Y = np.concatenate((np.ones(40), np.full(40, 2)));

for f in glob.glob('data/male0data/audio/tone1/*.wav'):
	dataArr = wf.read(f)
	pitchArr = pitchByWACF(dataArr)
	pitchArr = preprocess(pitchArr)
	#print "Pitch Array (after preprocess): "
	#print pitchArr
	m0t1pitch.append( pitchArr )


for f in glob.glob('data/male1data/audio/tone1/*.wav'):
	dataArr = wf.read(f)
	#m1t1wav.append( np.mean(dataArr[1], axis=1) )
	pitchArr = pitchByWACF(dataArr)
	pitchArr = preprocess(pitchArr)
	m1t1pitch.append( pitchArr )

for f in glob.glob('data/male0data/audio/tone2/*.wav'):
	dataArr = wf.read(f)
	#m0t2wav.append( np.mean(dataArr[1], axis=1) )
	pitchArr = pitchByWACF(dataArr)
	pitchArr = preprocess(pitchArr)
	m0t2pitch.append( pitchArr )

for f in glob.glob('data/male1data/audio/tone2/*.wav'):
	dataArr = wf.read(f)
	#m1t2wav.append( np.mean(dataArr[1], axis=1) )
	pitchArr = pitchByWACF(dataArr)
	pitchArr = preprocess(pitchArr)
	m1t2pitch.append( pitchArr )

print m0t1pitch

X = np.vstack([m0t1pitch, m1t1pitch, m0t2pitch, m1t2pitch])


clf = SVC()
print X
print Y
clf.fit(X, Y) 


file_Name = "jSVM.pkl"
print 'opening file'
fileObject = open(file_Name,'wb') 
joblib.dump(clf, fileObject) 

dataArr = wf.read('../wenUser.wav')
pitchArr = pitchByWACF(dataArr)
pitchArr = preprocess(pitchArr)

print clf.predict(pitchArr)