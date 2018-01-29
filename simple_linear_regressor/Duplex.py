import os
import csv
class mini_list:
	def __init__(self, label, data = []):
		self.label = label
		self.data = data
		self.index = []
		i = 0
		end = len(self.data)
		self.place = end
		while(i < end):
			self.index.append(i)
			i += 1


	def add_label(self, label):
		self.label = label

	def append_data(self, stuff):
		self.data.append(stuff)
		self.index.append(self.place)
		self.place +=1

	def get_data_point(self, place):
		return self.data[place]

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

	
##	def load_duplex(self, pathname):
##		with open(pathname) as tempfile:
##			reader = csv.reader(tempfile, delimieter=",")
##			colums = 0
##			self.lables = []
##			self.table = []
##			
##			cnt = 0
##			for line in reader:
##				if(cnt < 1):
##					columns = 0
##					nextpos = line.nextpos()
##					while(nextpos != "/n"):
##						self.labels.append(nextpos)
##						nextpos = line.nextpos()
##						columns += 1
##				
##				cnt += 1
##
##		tempfile.close()




