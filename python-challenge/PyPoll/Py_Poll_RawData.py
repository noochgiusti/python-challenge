import os
import csv

candidates = []
total_votes = 0
vote_counts = []

os.chdir(os.path.dirname(__file__))

election_data_csv = os.path.join('election_data.csv')
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    row = next(csvreader,None)

    for row in csvreader:

        total_votes = total_votes + 1
        
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1 
        else: 
            candidates.append(candidate)
            vote_counts.append(1)

        percentages = []
        max_votes = vote_counts[0]
        max_index = 0

        for count in range(len(candidates)): 
            vote_percentage = vote_counts[count]/total_votes*100
            percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
        winner = candidates[max_index]

percentages = [round(i,2) for i in percentages]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print(f"Winner: {winner}")

f = open("Text-Election-Results", "a")

f.write(f"\nElection Results")
f.write(f"\nTotal Votes: {total_votes}")
for count in range(len(candidates)):
    f.write(f"\n{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
f.write(f"\nWinner: {winner}")
    



