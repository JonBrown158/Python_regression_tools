import os
import csv

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

class Duplex:

	
	def __init__(self, first =[], second =[]):
		self.first = first
		self.second = second
		self.index = []
		i = 0
		end = len(self.first)
		self.place = end
		while(i < end):
			self.index.append(i)
			i += 1



	def get_first(self):
		return self.first
		
	def get_second(self):
		return self.second
	
	def getByValue(self, key):
		i = 0
		while(i < len(self.first)):
			if(key == self.first[i]):
				return self.second[i]
			i += 1
			
	def extend(self, first, second):
		self.first.append(first)
		self.second.append(second)
		self.index.append(self.place)
		self.place +=1
		
	def add_labels(self, first_label, second_label):
		self.first_label = first_label
		self.second_label = second_label

	




