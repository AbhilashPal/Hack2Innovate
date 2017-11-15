import csv
import pandas as pd

def setlabels(L):
	k=[]
	for i in L:
		if i == "0":
			k.append("ham")
		elif i == "1":
			k.append("spam")
		elif i == "2":
			k.append("info")
	print(len(k))
	return k
