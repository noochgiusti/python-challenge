import os
import csv

month_count = 0
months = []
profitLoss = 0
this_month_profitloss = 0
last_month_profitloss = 0
profitloss_changes = []

os.chdir(os.path.dirname(__file__))

budget_data_csv = os.path.join('budget_data.csv')

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        month_count = month_count + 1
        months.append(row[0])
        this_month_profitloss = int(row[1])
        profitLoss = profitLoss + this_month_profitloss
        if month_count > 1:
            profitloss_change = this_month_profitloss - last_month_profitloss
            profitloss_changes.append(profitloss_change)
        last_month_profitloss = this_month_profitloss


sum_profitloss = sum(profitloss_changes)
average_change = sum(profitloss_changes) / (month_count - 1)
max_change = max(profitloss_changes)
min_change = min(profitloss_changes)
max_month_index = profitloss_changes.index(max_change)
min_month_index = profitloss_changes.index(min_change)
best_month = months[max_month_index]
worst_month = months[min_month_index]


print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${profitLoss}")
print(f"Average Profit/Loss Change: ${average_change}")
print(f"Greatest Increase in Profits: {best_month} (${max_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${min_change})")


f = open("text_budget_data.txt", "a")

f.write(f"\nTotal Months: {month_count}")
f.write(f"\nTotal Revenue: ${profitLoss}")
f.write(f"\nAverage Profit/Loss Change: ${average_change}")
f.write(f"\nGreatest Increase in Profits: {best_month} (${max_change})")
f.write(f"\nGreatest Decrease in Losses: {worst_month} (${min_change})")
