import os
import csv
from collections import Counter  
#define your csv path and files
                
filepath = os.path.join(".", "budget_data_1.csv")
filepath2= os.path.join("." , "budget_data_2.csv")


with open(filepath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    totalMonths = 0



    for row in reader:  
        totalMonths += 1
        dateRow = str(row["Date"])
        revenueRow = int(row["Revenue"])
        total_rev = (int(row["Revenue"]))
    
    

print("Total Month ", str(totalMonths))
 
print("Total Revenue %d" % total_rev)

print(int(revenueRow))


