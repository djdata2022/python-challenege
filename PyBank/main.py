#import relevant libraries
import os
import csv

#create file path variables to process data file
file_path = os.path.join("Resources","budget_data.csv")
output_file_path = os.path.join("Analysis","output_report.txt")

#create empty lists to hold the values in the data file
date_list = []
profit_list = []
profit_diff = []

#open data file and read data line by line
with open(file_path, "r") as csv_file:
    csv_reader =csv.reader(csv_file, delimiter=",")
    #save header row as requested
    header_row = next(csv_reader)

    #iterate csv file from second row through to the end, adding dates
    #and profits to created lists
    for row in csv_reader:
        date_list.append(row[0])
        profit_list.append(int(row[1]))

#calculate sum of profit
profit_sum = sum(profit_list)

#calculate the number of months
num_months = len(date_list)

#calculate profit difference between items in list, place in profit_diff list
for n in range(1, len(profit_list)):
    profit_diff.append((profit_list[n]) - (profit_list[n-1]))

#calculate average profit loss, max and min
av_profit_loss = sum(profit_diff)/len(profit_diff)
max_profit = max(profit_diff)
min_profit = min(profit_diff)

#use index function to determine index for max and min; use to find corresponding dates
max_index = 1+profit_diff.index(max_profit)
min_index = 1+profit_diff.index(min_profit)

#create variable to hold report
output_report = (
f"Financial Analysis \n" 
f"____________________________________ \n"

f"Total Months: {num_months} \n"
f"Total: ${profit_sum} \n"
f"Average Change: ${av_profit_loss:.2f} \n"
f"Greatest Increase in Profits: {date_list[max_index]} (${max_profit}) \n"
f"Greatest Decrease in Profits: {date_list[min_index]} (${min_profit}) \n"
)

#print analysis to terminal
print(output_report)

#export text file with results
with open(output_file_path,"w") as txt_file:
    txt_file.write(output_report)
