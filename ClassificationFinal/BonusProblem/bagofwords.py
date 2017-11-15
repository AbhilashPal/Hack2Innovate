from sklearn.feature_extraction.text import CountVectorizer
import csv
def getbagofwords(t):
	for i in t:
		i = str(i)
	vectorizer = CountVectorizer()
	bagofwords = vectorizer.fit(t)
	bagofwords = vectorizer.transform(t)
	return bagofwords