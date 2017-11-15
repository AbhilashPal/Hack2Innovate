from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
import col1
import col2_temp
import setlabel
import wr
import col3
import bagofwords

sms_list = col2_temp.getbow()
bagofw = bagofwords.getbagofwords(sms_list)
# smses
X = bagofw

Y_labels = col1.getlabels()
# spam,info,ham
Y = Y_labels
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
test_list = col3.testdata()
bagofwordsdash = bagofwords.getbagofwords(test_list)
prediction = clf.predict(bagofwordsdash)
labelized = setlabel.setlabels(prediction)
print (labelized)
wr.writetocsv(labelized)