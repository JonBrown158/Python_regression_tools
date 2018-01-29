import os
import csv
from Duplex import Duplex

class Loader:

	def __init__(self):
		pass
		
	def loadDuplexFromFile(self, filename, pos1 = 0, pos2 = 1):		
		data = Duplex()
		with open(filename) as tempfile:
			reader = csv.reader(tempfile, delimiter=",")
			
			i = 0
			for line in reader:
				if(i<1):
					data.add_labels(line[pos1], line[pos2])
				else:
					data.extend(line[pos1], float(line[pos2]))
				i +=1
		tempfile.close()
		return data
