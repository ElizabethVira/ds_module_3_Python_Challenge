# Calculate the following information for a vote counting process for small rural town
# Total numbers of votes, (line 26, sume of votes)
# Total list of candidates with votes
# Percentage of votes per candidate won
# Total of votes fore each canidate won
# The winner
    # Module for reading CSV files and set path for file

import csv
csvpath = "PyPoll/Resources/election_data.csv"

# Set the variable
vote_count = 0

# Set a variable for each candidate
C1 = 0
C2 = 0
C3 = 0

# Open the CSV using the UTF-8 encoding (previus classes code)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (previus classes code)
    csv_header = next(csvreader)

    for row in csvreader:
        
        vote_count += + 1

        if ((row [2]) == ("Charles Casper Stockham")):
            C1 += 1
        elif ((row[2]) == ("Diana DeGette")):
            C2 += 1
        else:
            C3 += 1


percentC1 = C1 / vote_count *100
percentC2 = C2 / vote_count *100
percentC3 = C3 / vote_count *100


winner = ""

if (percentC1 > percentC2) and (percentC1 > percentC3):
    winner = "Charles Casper Stockham"
elif(percentC2 > percentC1) and (percentC2 > percentC3):
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"


output = (

    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_count}\n"
    f"-------------------------\n"
    f"Charles Casper Stockham: {percentC1:.3f}% ({C1})\n"
    f"Diana DeGette: {percentC2:.3f}% ({C2})\n"
    f"Raymon Anthony Doane: {percentC3:.3f}% ({C3})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
print(output)

# Creating a text file
with(open("output_PyPoll.txt", "w") as f):
    f.write(output)
