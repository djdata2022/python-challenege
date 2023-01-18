#import relevant libraries
import os
import csv
file_path = os.path.join("Resources","budget_data.csv")

date_list = []
profit_list = []
profit_sum = 0

with open(file_path, "r") as csv_file:
    csv_reader =csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        date_list.append(row[0])
        profit_list.append(row[1])
        profit_sum = profit_sum + int(row[1])

num_months = len(date_list)
print()

#I DON'T UNDERSTAND HOW TO CALC THIS
change_profit_loss = int(profit_list[num_months]) - int(profit_list[0])
av_profit_loss = change_profit_loss/num_months

#print(change_profit_loss)

print("""
Financial Analysis
____________________________________
""")

print(f"Total Months: {num_months}")
print(f"Total: ${profit_sum}")
print(f"Average Change: ${av_profit_loss}")