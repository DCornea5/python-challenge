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
averagechanges=0
greatestmnthinc=0
greatestmnthdec=0
greatestinc=0
greatestdec=0
profitmnth=0
greatestincp=0

with open(path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        months += 1
        profits += int(row[1])

  
        #monthcrt = int(row[1])
        #changes=monthcrt-monthprev
        #mntprev=int(row[1])
      
        if int(row[1]) > greatestinc:
            greatestinc=int(row[1])
            greatestmnthinc=row[0]
            
        elif int(row[1])< greatestdec:
            greatestdec=int(row[1])
            greatestmnthdec=row[0]

        
        changes=monthcrt-greatestincp
        monthcrt=int(row[1])

  
print("Financial Analysis")
print("-------------------") 
print("Total Months: "+str(months))  
print("Total Profit/Losses: $"+str(profits))  
print("Average Change: $"+str(averagechanges)) 
print("Greatest Increase in Profit: "+greatestmnthinc+ "($" + str(greatestinc)+")")
print("Greatest Decrease in Profit: "+greatestmnthdec+"($" + str(greatestdec) + ")") 

Financials=os.path.join("Financial Analysis.txt")
with open(Financials,"w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write("Total Months: "+str(months)+"\n")
    file.write("Total Profit/Losses: $"+str(profits)+"\n")
    file.write("Average Change: $"+str(averagechanges)+"\n") 
    file.write("Greatest Increase in Profit: "+greatestmnthinc+ "($" + str(greatestinc)+")"+"\n")
    file.write("Greatest Decrease in Profit: "+greatestmnthdec+"($" + str(greatestdec) + ")"+"\n") 