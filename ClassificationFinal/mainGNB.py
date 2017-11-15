from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
import col1
import col2
import setlabel
import wr
import col3
import bagofwords
import bagofwordsnew
from sklearn import metrics

sms_list = col2.getbow()
# smses
bagofwords1 = bagofwords.getbagofwords(sms_list)
X = bagofwords1[0:30000]
# spam,info,ham
Y_labels = col1.getlabels()
Y = Y_labels[0:30000]
clf = KNeighborsClassifier(3)
clf = clf.fit(X,Y)
#ok till here
test_list = bagofwords1[30000:37500]
#Problem Starts from here :
bagofwords2 = test_list
print(bagofwords2)

#Working fine 
prediction = clf.predict(bagofwords2)
labelized = setlabel.setlabels(prediction)
print (len(labelized))
wr.writetocsv(labelized)