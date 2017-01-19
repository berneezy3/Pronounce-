import pickle
import cPickle
import scipy.io.wavfile as wf 
from sklearn.externals import joblib
from weightedAutoCor import *
from preprocess import *


pkl_file = open('jSVM.pkl', 'rb')

SVM = joblib.load(pkl_file)

dataArr = wf.read('../zhongWrong.wav')
pitchArr = pitchByWACF(dataArr)
pitchArr = preprocess(pitchArr)

print pitchArr
print SVM.decision_function(pitchArr)
print SVM.predict(pitchArr)

dataArr = wf.read('../wenWrong.wav')
pitchArr = pitchByWACF(dataArr)
pitchArr = preprocess(pitchArr)

print pitchArr
print SVM.decision_function(pitchArr)
print SVM.predict(pitchArr)