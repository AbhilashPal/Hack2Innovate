import pandas as pd
import numpy as np 
def getlabels():
	k = []
	data = pd.read_csv("TRAIN_SMS.csv", usecols = [0])
	l = (data.to_string(index=False)).split("\n")
	for i in l:
		if i == " ham":
			k.append("0")
		elif i == "spam":
			k.append("1")
		elif i == "info":
			k.append("2")
	return k
