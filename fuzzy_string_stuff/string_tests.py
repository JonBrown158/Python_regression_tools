from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from data_table import Data_table
import csv 


titles = Data_table('deals',',')

print("number of rows {}".format(titles.num_rows))

Names = titles.get_column('title')
UUID = titles.get_column('uuid')
Price = titles.get_column('price')
Description = titles.get_column('description')
print(titles.order, '\n')
print('num_fiiles {}'.format(titles.files_loaded))


print("\n\n\n")


row = 3 
sensitivity = 75

target = titles.rows[row][Names]
time_published = 'none'
last_uuid = 'none'
print("matches for {} are".format(target))

i = 0
while(i < titles.num_rows):
	if(fuzz.ratio(titles.rows[i][Names], target) > sensitivity):
		print(titles.rows[i][Names], 'uuid {}'.format(titles.rows[i][UUID]),'price {}'.format(titles.rows[i][Price]), i)
		
	i +=1






