import os
from os import listdir
import csv


def find_csv_filenames(path_to_dir, suffix = ".csv"):
	filenames = listdir(path_to_dir)
	return [filename for filename in filenames if filename.endswith(suffix)]

class Data_table:
	## sets original file into data table then uses it's indecies to sort addtions to table
	def __init__(self, path, delm):
		## used to order unordered lists from database
		self.order =[]
		## each row of data is stored in rows
		self.rows = []
		## used to give indexes for new inputs from diffrent files
		self.tempindex = []
		## used to seperate lables from for columns from rows of data
		self.firstpass = True
		## char to use for seperating data
		self.delm = delm
		## used to determine first file
		self.firstfile = True
		## used to count number of files loaded
		self.files_loaded = 0
		
		
		## list of .csv files
		self.file_names = find_csv_filenames(path, suffix = ".csv")
	
		
		for files in self.file_names:
			if self.firstfile:
				self.load_initial_file(path + "//" + files, self.delm)
				self.firstfile = False
				self.files_loaded += 1
			else:
				self.add_to_table(path + "//" + files, self.delm)
				self.files_loaded += 1
		
	
	def load_initial_file(self, path, delm):
		self.firstpass = True
		
		with open(path, 'r') as tempfile:		
			
			csvfile = csv.reader(tempfile, delimiter = delm)

			for row in csvfile:
				if self.firstpass:
					self.order = row
					self.firstpass = False
				else:
					self.rows.append(row)
				
				

		self.num_rows = len(self.rows)
		self.num_col = len(self.rows[0])
		
		tempfile.close()
	
	## adds next file into table using the indecies from the initial file opened
	def add_to_table(self, path, delm):
		
		self.firstpass = True

		with open(path, 'r') as tempfile:		
			
			csvfile = csv.reader(tempfile, delimiter = delm)

			for row in csvfile:
				if self.firstpass:
					self.get_order(row)
					self.firstpass = False
				else:
					row = [row[i] for i in self.tempindex]
					self.rows.append(row)
				
				

		self.num_rows = len(self.rows)
		
		tempfile.close()
				

	## used to get the substitution box for the new file being added so that they are in the order of the
	## rest of the files
	def get_order(self, row):
		
		self.tempindex = []
		for lable in row:
			self.tempindex.append(self.order.index(lable))
		j = 0
		invert_od = []
		for i in self.tempindex:
			invert_od.append(self.tempindex.index(j))
			j += 1
		self.tempindex = invert_od

	## returns index of a particular column must be used because there is no guarantee that any column 
	## will be in a particular place 
	def get_column(self, column):
		return self.order.index(column)


