#	The total number of votes cast 3521001
#	A complete list of candidates who received votes
#	The percentage of votes each candidate won
#	The total number of votes each candidate won
#	The winner of the election based on popular vote •	Winner: Khan

import os
import csv
from typing import List
pypollpath=os.path.join("Resources","election_data.csv")



totalvotes=0
with open(pypollpath, newline="") as csvfile:
    csvreaderp=csv.reader(csvfile, delimiter=",")
    csvheaderp=next(csvreaderp)
    Correyvotes=0
    Khanvotes=0
    Livotes=0
    Otooleyvotes=0

    list=["Voter ID", "County", "Candidate"]
    for row in csvreaderp:
        totalvotes += 1
        if row[2] =="Correy":
            Correyvotes +=1
        elif row[2] =="Khan":
            Khanvotes += 1
        elif row[2] =="Li":
            Livotes +=1   
        elif row[2] =="O'Tooley":
            Otooleyvotes +=1    

    Correyper=format((Correyvotes/totalvotes)*100,".3f")
    Khanper=format((Khanvotes/totalvotes)*100,".3f")
    Liper=format((Livotes/totalvotes)*100,".3f")
    Otooleyper=format((Otooleyvotes/totalvotes)*100,".3f")



    candidateslist= ["Correy",
    "Khan",
    "Li",
    "Otooley"]
            
    voteslist= ["Correyvotes", 
    "Khanvotes",
    "Livotes",
    "Otooleyvotes"]     

print("Election Results\n")  
print("-----------------------\n") 
print("Total Votes:"+str(totalvotes)+"\n") 
print("-----------------------\n")
print(f"Khan: {Khanper}% ({Khanvotes})")
print(f"Coorey: {Correyper}% ({Correyvotes})")
print(f"Li: {Liper}% ({Livotes})")
print(f"Otooley: {Otooleyper}% ({Otooleyvotes})")
print(f"Winner: ")
print("-----------------------\n") 

Votes=os.path.join("Election Results.txt")

with open(Votes,"w") as file:

    file.write("Election Results\n")  
    file.write("-----------------------\n") 
    file.write("Total Votes:"+str(totalvotes)+"\n") 
    file.write("-----------------------\n")
    file.write(f"Khan: {Khanper}% ({Khanvotes})\n")
    file.write(f"Coorey: {Correyper}% ({Correyvotes})\n")
    file.write(f"Li: {Liper}% ({Livotes})\n")
    file.write(f"Otooley: {Otooleyper}% ({Otooleyvotes})\n")
    file.write(f"Winner: \n")
    file.write("-----------------------\n") 
