# 	PyPoll Challenge
#   The total number of votes cast 
#	A complete list of candidates who received votes
#	The percentage of votes each candidate won
#	The total number of votes each candidate won
#	The winner of the election based on popular vote 

# import modules for Python interaction with operating system and comma separated files 
import os
import csv
from typing import List
pypollpath=os.path.join("Resources","election_data.csv")

#open csv file and calculate total votes each candidate won
totalvotes=0
with open(pypollpath, newline="") as csvfile:
    csvreaderp=csv.reader(csvfile, delimiter=",")
    csvheaderp=next(csvreaderp)
    Correyvotes=0
    Khanvotes=0
    Livotes=0
    Otooleyvotes=0
    popularvote=0

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

    # calculate percentages of votes each candidate won
    Correyper=format((Correyvotes/totalvotes)*100,".3f")
    Khanper=format((Khanvotes/totalvotes)*100,".3f")
    Liper=format((Livotes/totalvotes)*100,".3f")
    Otooleyper=format((Otooleyvotes/totalvotes)*100,".3f")

    # create a dictionary to match candidates with votes, to be used for finding the winner    
    candidateslist= ["Correy",
    "Khan",
    "Li",
    "Otooley"]
            
    voteslist= [Correyvotes, 
    Khanvotes,
    Livotes,
    Otooleyvotes]     
    
    dictionary={}
    for candidate in candidateslist:
        for votes in voteslist:
            dictionary[candidate]=votes
            voteslist.remove(votes)
            break
    # find teh winner
    max=max(dictionary.values())
    for candidate, votes in dictionary.items():
        if votes==max:
            Winner=candidate

# print results to terminal        
print("Election Results\n")  
print("-----------------------\n") 
print("Total Votes:"+str(totalvotes)+"\n") 
print("-----------------------\n")
print(f"Khan: {Khanper}% ({Khanvotes})")
print(f"Coorey: {Correyper}% ({Correyvotes})")
print(f"Li: {Liper}% ({Livotes})")
print(f"Otooley: {Otooleyper}% ({Otooleyvotes})\n")
print(f"Winner: {Winner}")
print("-----------------------\n") 

# prepare and export a text file with the results
Votes=os.path.join("Election Results.txt")

with open(Votes,"w") as file:

    file.write("Election Results\n")  
    file.write("-----------------------\n") 
    file.write("Total Votes: "+str(totalvotes)+"\n") 
    file.write("-----------------------\n")
    file.write(f"Khan:    {Khanper}% ({Khanvotes})\n")
    file.write(f"Coorey:  {Correyper}% ({Correyvotes})\n")
    file.write(f"Li:      {Liper}% ({Livotes})\n")
    file.write(f"O'Tooley: {Otooleyper}% ({Otooleyvotes})\n")
    file.write(f"Winner:  {Winner}\n")
    file.write("-----------------------\n") 
