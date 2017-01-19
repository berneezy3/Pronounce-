import pickle
import cPickle
import scipy.io.wavfile as wf 
from sklearn.externals import joblib
from MLSP import weightedAutoCor as WAC
from MLSP import preprocess as pp

pkl_file = open('MLSP/jSVM.pkl', 'rb')

print pkl_file
SVM = joblib.load( pkl_file )

dataArr = wf.read('zhongWrong.wav')
print dataArr
pitchArr = WAC.pitchByWACF(dataArr)
pitchArr = pp.preprocess(pitchArr)

print pitchArr
print SVM.decision_function(pitchArr)
print SVM.predict(pitchArr)

dataArr = wf.read('wenWrong.wav')
pitchArr = WAC.pitchByWACF(dataArr)
pitchArr = pp.preprocess(pitchArr)

print pitchArr
print SVM.decision_function(pitchArr)
print SVM.predict(pitchArr)