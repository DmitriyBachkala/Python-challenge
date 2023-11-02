import csv

# Define file paths
# Input
input_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyPoll/Resources/election_data.csv"

# Output
output_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyPoll/Analysis/election_results.txt"

# Initialize variables to store election data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(input_file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract data from each row
        voter_id = row[0]
        candidate = row[2]

        # Calculate the total number of votes
        total_votes += 1

        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner and their vote count
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Generate the election results report
election_results = f"Election Results\n{'-' * 25}\nTotal Votes: {total_votes}\n{'-' * 25}\n"

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    election_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

election_results += f"{'-' * 25}\nWinner: {winner}\n{'-' * 25}"

# Print the analysis to the terminal
print("")
print(election_results)
print("")

# Export the results to the specified output file
with open(output_file_path, 'w') as file:
    file.write(election_results)