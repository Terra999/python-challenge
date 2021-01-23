# Dear Grader - I'll be honest - most of this code was made possible because of help 
# from the following people: Stephanie Richards - she posted her code(!), Beau Jeffrey, Melissa Lowe and as always Sharon Templin.
# I understand things in small chunks, I just don't get how they all go together. I'll keep trying though!

# Import modules
import os
import csv

#Find file
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Define variables
    total_votes = 0
    candidate_name = []
    

    # Read through each row of data after header
    for row in csvreader:

        # Find total number of votes
        total_votes = total_votes + 1

        # Where to find candidate names to put inside the list
        candidate_name.append(str(row[2]))

# Define variables
unique_candidates = []
candidate_votes = []
vote_count = 0

# Set up a function to find unique candidate name
def unique(candidate_name):
    
    # Read through each row
    for name in candidate_name:
         if name not in unique_candidates:
                unique_candidates.append(name)
    return unique_candidates

# Return unique candidate names
unique(candidate_name)
 # print(unique_candidates)

# Set parameter for vote count
def vote_count(unique_candidates):
    # Set counter to 0
    vote_count = 0

    # Go row by row looking for candidate name
    for name in unique_candidates:
        # Then compare to find number of votes
        for vote in candidate_name:
            #If they match up then add to vote count
            if name == vote:
                vote_count = int(vote_count) + 1
        # Add to vote_count list
        candidate_votes.append(vote_count)
        # Reset counter
        vote_count = 0
    return candidate_votes

vote_count(unique_candidates)
# print(candidate_votes)

# Find the winner
win_vote = max(candidate_votes)
win_index = candidate_votes.index(win_vote)
winner = unique_candidates[win_index]
# print(winner)

# Find candidate vote percent - I almost figured this out by myself!
candidate_vote_percent = []
for x in (candidate_votes):
    vote_percent = round((float(int(x) / int(total_votes)) * 100), 3)
    candidate_vote_percent.append(vote_percent)
# print(candidate_vote_percent)

#zip lists to make tuple - Yay! I actually understand the tuple part! Needed help printing the candidate_tuple below though.
candidate_tuple = tuple(zip(unique_candidates, candidate_vote_percent, candidate_votes))
        

print(" ")
print("Election Results")       
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for lst in candidate_tuple:
    print(f"{lst[0]}: {lst[1]}00% ({lst[2]})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")