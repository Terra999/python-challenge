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

    # Identify variables
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

# Set up a function to find unique
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
    # 
    for name in unique_candidates:
        for vote in candidate_name:
            if name == vote:
                vote_count = int(vote_count) + 1
        candidate_votes.append(vote_count)
        vote_count = 0
    return candidate_votes

vote_count(unique_candidates)
print(candidate_votes)

# def print_percentages(candidate_votes):

#     candidate_votes = 0
#     unique_candidates = 0 

#     win_percent = round(candidate_votes / unique_candidates * 100, 2)

#     print(win_percent)




        

        

        


print("Election Results")       
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")