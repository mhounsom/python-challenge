import os
import csv


csvpath = os.path.join(".", "PyPoll", "Resources", "election_data.csv")

total_votes_overall = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


with open(csvpath, newline = '') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:

        total_votes_overall = total_votes_overall + 1

        if (row[2] == "Khan"):
            khan_votes = khan_votes + 1
        elif (row[2] == "Correy"):
            correy_votes = correy_votes + 1
        elif (row[2] == "Li"):
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1

    khan_percentage = khan_votes/total_votes_overall
    correy_percentage = correy_votes/total_votes_overall
    li_percentage = li_votes/total_votes_overall
    otooley_percentage = otooley_votes/total_votes_overall

    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        name = "Khan"
    elif winner == correy_votes:
        name = "Correy"
    elif winner == li_votes:
        name = "Li"
    else:
        name = "O'Tooley"
        

       




print("Election Results")        
print("-----------------------------------")
print(f"Total Votes: {total_votes_overall}")
print("-----------------------------------")
print(f"Khan: {khan_percentage:.3%} ({khan_votes})")
print(f"Correy: {correy_percentage:.3%} ({correy_votes})")
print(f"Li: {li_percentage:.3%} ({li_votes})")
print(f"O'Tooley: {otooley_percentage:.3%} ({otooley_votes})")
print("-----------------------------------")
print(f"Winner: {name}")
print("-----------------------------------")

output_file = os.path.join(".", "PyPoll", "analysis", "pypoll_results.text")
with open(output_file, 'w',) as txtfile:

    txtfile.write("Election Results\n")        
    txtfile.write("-----------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes_overall}\n")
    txtfile.write("-----------------------------------\n")
    txtfile.write(f"Khan: {khan_percentage:.3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percentage:.3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percentage:.3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percentage:.3%} ({otooley_votes})\n")
    txtfile.write("-----------------------------------\n")
    txtfile.write(f"Winner: {name}\n")
    txtfile.write("-----------------------------------\n")