import csv
def writetocsv(L):
	returns_path = "D:\mlclass\Hack2Innovate\ClassificationFinal\TEST_RESULT.csv"
	file = open(returns_path,'w')
	writer = csv.writer(file)
	writer.writerow(["RecordNo","Label"],)
	for i in range(len(L)-1):
		RecordNo = i+1
		Label = L[i]
		writer.writerow([RecordNo,Label],)