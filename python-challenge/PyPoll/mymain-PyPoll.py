
#First Import your csv file
import os
import csv

pypoll_csv = os.path.join("Resources", "election_data.csv")

# the below text is to replicate how the results are displayed in the example
print("Election Results")
srting_break = "-----------------------------"
print(srting_break)

# open csv file and begin 
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # script below moves to the next row of data so the header is not included
    csv_header = next(csvreader)

    # below syntax is to define variables before beginning our for loop
    total_votes = 0
    # below creates a list of candidates
    candidate_list = []
    # below creates a dictionary 
    candidate_votes = {}
    winning_votes = 0
    # below will save the winner as a string
    winner = ''
    
    
    for row in csvreader:
        
        # count each row of data after the header to obtain the total votes value
        total_votes += 1
        
        candidate = row[2]   
        
        # finding the Total Number of votes cast
        if candidate not in candidate_list:
            
            #below creates the list of candidates
            candidate_list.append(candidate)
            
            # first step in creating our dictionary
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1
    
    #Print The Total Number of Votes Cast
    print(f"Total Votes: {total_votes}") 
    
    print(srting_break)
    
    # connecting the candidate name to the amount of votes each candidate obtained
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        
        percentage_votes = (votes / total_votes) * 100
        
        # the example images were rounded to three decimal places
        # syntax to round found on ChatGPT
        rounded_percentage = round(percentage_votes, 3)
        
        # last if statement to find the winner
        # loop until we are left with the candidate with the most votes
        if votes > winning_votes:
            
            winning_votes = votes
            
            winner = candidate
        
        # Print the summary table of Candidate Votes
        # This includes the canidates who recieved votes, percentage of votes eah canidate won, and total number of votes per canidate
        print(f"{candidate}: {rounded_percentage}% ({votes})")

    
    print(srting_break)
    
    #Print the Winner of the electrion based on popular vote
    print(f"Winner: {winner}")
    
print(srting_break)