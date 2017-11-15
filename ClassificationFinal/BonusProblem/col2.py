import pandas as pd
import numpy as np 
import csv

def getbow():
	path = "TRAIN_info_SMS.csv"
	file = open(path,newline="")
	reader = csv.reader(file)
	header = next(reader)
	message=[]
	for i in reader:
		message.append(i[1])
	return message