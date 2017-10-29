import csv

# Files to load and output (Remember to change these)
file_to_load = "election_data_2.csv"
#file_to_output = "election_analysis_1.txt"

# Read the csv and convert it into a reader

with open(file_to_load,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)[1:] 

Voter_ID = []
Can_Vote = []

for row in data:
# Populate revenue list and slice out the header
    Voter_ID.append((row[0]))

#for row in data:
# Populate revenue list and slice out the header
    Can_Vote.append((row[2]))

# Determine the total number of vote

Total_Votes = len(Can_Vote)
Total_Votes = int(Total_Votes)

# Determine the unique candidate names by creating a set
Candidate_Set = set(Can_Vote)
names = []

for row in Candidate_Set:
    names.append(row)

# Start Printing the output

print(" Election Results   ")

print( "---------------------")

print("Total Number of Votes -  ", Total_Votes)

# Set up a loop to print out the candidates and votes

can = 0
Candidate_Dictionary = {}

for row in names:
    candidate = str(names[can])
    Votes = Can_Vote.count(candidate)
    Votes = int(Votes)
    percentage = Votes / Total_Votes * 100
    Candidate_Dictionary.update({ candidate : Votes})
    print(candidate, ":  ", percentage, " %  (", Votes, ")" )
    can = can + 1

print( "")
print("Winner:  ", max(Candidate_Dictionary()))