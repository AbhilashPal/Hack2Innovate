from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
import col1
import col2
import setlabel
import wr
import col3
import bagofwords
import numpy as np

sms_list = col2.getbow()
# smses
bagofwords1 = bagofwords.getbagofwords(sms_list)
X = bagofwords1[0:12000]
print ("Bag1:",bagofwords1)
# spam,info,ham
Y_labels = col1.getlabels()
Y = Y_labels
clf = MLPClassifier(alpha=1)
clf = clf.fit(X,Y)
#ok till here
test_list = bagofwords1[12000:15000]
#Problem Starts from here :
bagofwords2 = test_list
print("Bag2:",bagofwords2)
#Working fine 
prediction = clf.predict(bagofwords2)
labelized = setlabel.setlabels(prediction)
print (len(labelized))
wr.writetocsv(labelized)
