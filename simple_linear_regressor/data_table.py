import os
import csv

class Data_table:
	
	def __init__(self, path):
		self.rows = []
		
		with open(path) as tempfile:
			csvfile = open(path, 'rb')
			
			for row in csv.reader(csvfile, delimiter = ','):	
				self.rows.append(row)
				
				

		self.num_rows = len(self.rows)
		self.lables = self.rows[0]
		self.num_col = len(self.rows[0])

