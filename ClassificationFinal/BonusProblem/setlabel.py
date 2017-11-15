import csv
import pandas as pd

def setlabels(L):
	k=[]
	for i in L:
		if i == "0":
			k.append("Delivery")
		elif i == "1":
			k.append("Hotel")
		elif i == "2":
			k.append("Payment")
		elif i == "3":
			k.append("Appointment")
		elif i == "4":
			k.append("Train")
		elif i == "5":
			k.append("PickUp")
		elif i == "6":
			k.append("Flight")
		elif i == "7":
			k.append("Movie")
		elif i == "8":
			k.append("Bus")
		elif i == "9":
			k.append("Expiry")
		elif i == "10":
			k.append("Reservation")
		elif i == "11":
			k.append("Cab")
	print(len(k))
	return k
