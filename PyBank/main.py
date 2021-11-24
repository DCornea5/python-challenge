import os
import csv
cwd = os.getcwd()
#print(cwd)

path = os.path.join("Resources","budget_data.csv")

months=0
monthcrt=0
monthprev=0
profits=0
changestotal=0
changes=[]

with open(path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        months += 1
        profits += int(row[1])
        monthcrt += int(row[1])
        changes.append(monthcrt-monthprev)
        monthprev=int(row[1])

print("Financial Analysis")
print("-------------------") 
print("Total Months: "+str(months))  
print("Total Profit/Losses: "+str(profits))  
print("Average Change: $" ) 




    
