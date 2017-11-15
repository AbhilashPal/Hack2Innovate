import pandas as pd
import numpy as np 
def getlabels():
	k = []
	data = pd.read_csv("TRAIN_info_SMS.csv", usecols = [0])
	l = (data.to_string(index=False)).split("\n")
	n = 0
	for i in l:
		n+=1
		if i == "   Delivery":
			k.append("0")
		elif i == "      Hotel":
			k.append("1")
		elif i == "    Payment":
			k.append("2")
		elif i == "Appointment":
			k.append("3")
		elif i == "      Train":
			k.append("4")
		elif i == "     PickUp":
			k.append("5")
		elif i == "     Flight":
			k.append("6")
		elif i == "      Movie":
			k.append("7")
		elif i == "        Bus":
			k.append("8")
		elif i == "     Expiry":
			k.append("9")
		elif i == "Reservation":
			k.append("10")
		elif i == "        Cab":
			k.append("11")
		else:
			k.append(i)
		if n==12000:
			break
	return k
