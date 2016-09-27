import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from pandas import Series,DataFrame

def read_file_by_iteration(file_name):
    retail_list = []
    with open (file_name) as my_file:
        for line in my_file:
            retail_list.append(line.strip('\n'))
    return retail_list

retail = read_file_by_iteration('retail.csv')
report = read_file_by_iteration('reported.csv')

with open('results.txt','w') as f:
	for item in report:
		results = process.extract(item,retail)
     	f.write("%s\n" % str(results))
