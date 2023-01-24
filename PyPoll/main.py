#import relevant libraries
import os
import csv

#create variables to process data file
file_path = os.path.join("Resources","election_data.csv")
output_file_path = os.path.join("Analysis","output_report.txt")

#create empty lists to hold the values/columns in the data file
voter_list = []
county_list = []
candidate_list = []

#create variable for total profit and total profit difference and set to zero
#profit_sum = 0
#profit_diff_sum = 0

#open data file and read data line by line
with open(file_path, "r") as csv_file:
    csv_reader =csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    #iterate csv file from second row through to the end, adding items to lists
    for row in csv_reader:
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])
        #calculate the sum of profit
        #profit_sum = profit_sum + int(row[1])

#calculate total number of votes cast
total_votes=len(voter_list)

print(total_votes)

#create complete list of candidates who received votes
unique_candidates = []

for item in candidate_list:
    if item not in unique_candidates:
        unique_candidates.append(item)

print(unique_candidates)

#create empty list for counts
votes_per_candidate = []

#count number of each candidate
for candidates in unique_candidates:
    count=candidate_list.count(candidates)
    votes_per_candidate.append(count)

print(votes_per_candidate) # remove before final

#create empty list to hold vote percentages
percent_vote = []

#calculate percentages
for x in votes_per_candidate:
    percentage = 100*int(x)/int(total_votes)
    percent_vote.append(percentage)
    
print(percent_vote) # remove before final

#create combined file of summary results - candidate, votes, percent
combined_file = zip(unique_candidates,votes_per_candidate, percent_vote)

print(combined_file) #remove before finalizing

winner_index = votes_per_candidate.index(max(votes_per_candidate))


#create variable to hold report
output_report = (
f"Election Results \n"
f"____________________________________ \n"
f"Total Votes: {total_votes} \n"
f"____________________________________ \n"
f"{unique_candidates[0]}: {percent_vote[0]:.3f}% ({votes_per_candidate[0]}) \n"
f"{unique_candidates[1]}: {percent_vote[1]:.3f}% ({votes_per_candidate[1]}) \n"
f"{unique_candidates[2]}: {percent_vote[2]:.3f}% ({votes_per_candidate[2]}) \n"
f"____________________________________ \n"
f"Winner: {unique_candidates[winner_index]} \n"
f"____________________________________ \n"
)

#print analysis to terminal
print(output_report)

#for row in combined_file:
#    print(
#f"{row[0]} ": " {row[1]} \n"
#f"Average Change: ${av_profit_loss}\n"
#f"Greatest Increase in Profits: ${max_profit}\n"
#f"Greatest Decrease in Profits: ${min_profit}\n"




#export text file with results **REMOVE COMMENTS BELOW BEFORE SUBMITTING**
#with open(output_file_path,"w") as txt_file:
#    txt_file.write(output_report)
