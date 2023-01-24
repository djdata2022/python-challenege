#import relevant libraries
import os
import csv

#create variables to process data file
file_path = os.path.join("Resources","budget_data.csv")
output_file_path = os.path.join("Analysis","output_report.txt")

#create empty lists to hold the values/columns in the data file
date_list = []
profit_list = []
profit_diff = []

#create variable for total profit and total profit difference and set to zero
profit_sum = 0
profit_diff_sum = 0

#open data file and read data line by line
with open(file_path, "r") as csv_file:
    csv_reader =csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    #iterate csv file from second row through to the end, adding dates
    #and profits to new lists
    for row in csv_reader:
        date_list.append(row[0])
        profit_list.append(int(row[1]))
        #calculate the sum of profit
        #profit_sum = profit_sum + int(row[1])

profit_sum = sum(profit_list) #**could also do this after making list integer?**

#calculate the number of months
num_months = len(date_list)

#calculate profit difference between items in list
for n in range(1, len(profit_list)):
    profit_diff.append((profit_list[n]) - (profit_list[n-1]))

#Calc av profit loss, max and min
av_profit_loss = sum(profit_diff)/len(profit_diff)
max_profit = max(profit_diff)
min_profit = min(profit_diff)

#combine dates and profit change in one file
combined_file = zip(date_list,profit_diff)

#create variable to hold report ***2 DP, ADD DATES FOR MAX, MIN**
output_report = (
f"Financial Analysis \n" 
f"____________________________________ \n"

f"Total Months: {num_months} \n"
f"Total: ${profit_sum}\n"
f"Average Change: ${av_profit_loss:.2f} \n"
f"Greatest Increase in Profits: {date_list[index]} ${max_profit}\n"
f"Greatest Decrease in Profits: ${min_profit}\n"
)

#print analysis to terminal
print(output_report)

#export text file with results **REMOVE COMMENTS BELOW BEFORE SUBMITTING**
#with open(output_file_path,"w") as txt_file:
#    txt_file.write(output_report)
