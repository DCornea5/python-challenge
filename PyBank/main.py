# import modules for operating system and comma separated files
import os
import csv
#path for the CSV file
path = os.path.join("Resources","budget_data.csv")

#create variables
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


# open the csv file 
with open(path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    #loop through the csv file to calculate the total months and total profits
    for row in csvreader:
        months += 1
        profits += int(row[1])
        mnthcrt=int(row[1])
        changes.append(monthcrt-monthprev)   
        monthprev=int(row[1]) 
           
        #look for the greatest increase and decrease
        if int(row[1]) > greatestinc:
            greatestinc=int(row[1])
            greatestmnthinc=row[0]
           
        if int(row[1])< greatestdec:
            greatestdec=int(row[1])
            greatestmnthdec=row[0]


        
#print the results in terminal     
print("Financial Analysis")
print("-------------------") 
print("Total Months: "+str(months))  
print("Total Profit/Losses: $"+str(profits))  
print("Average Change: $"+str(averagechanges)) 
print("Greatest Increase in Profit: "+greatestmnthinc+ "($" + str(greatestinc) +")")
print("Greatest Decrease in Profit: "+greatestmnthdec+"($" + str(greatestdec) + ")") 

#create and update a txt file with the results of the analysis
Financials=os.path.join("AnalysisPyBank","Financial Analysis.txt")
with open(Financials,"w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write("Total Months: "+str(months)+"\n")
    file.write("Total Profit/Losses: $"+str(profits)+"\n")
    file.write("Average Change: $"+str(averagechanges)+"\n") 
    file.write("Greatest Increase in Profit: "+greatestmnthinc+ "($" + str(greatestinc)+")"+"\n")
    file.write("Greatest Decrease in Profit: "+greatestmnthdec+"($" + str(greatestdec) + ")"+"\n")