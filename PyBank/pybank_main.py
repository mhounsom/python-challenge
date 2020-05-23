import os
import csv


csvpath = os.path.join(".", "PyBank", "Resources", "budget_data.csv")

monthly_revenue_change = []
date = []
total_revenue = 0
total_months = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

with open(csvpath, newline = '') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    csv_header = next(csvreader)

    previous_profit_loss = int(csv_header[1])
    total_months = total_months + 1 
    total_revenue = total_revenue + int(csv_header[1]) 

    for row in csvreader:

        total_months = total_months + 1 

        total_revenue = total_revenue + int(row[1])

        monthly_change = int(row[1]) - previous_profit_loss
        monthly_revenue_change.append(monthly_change)
        previous_profit_loss = int(row[1])
        date.append(row[0])

    
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

            high = max(monthly_revenue_change)
            low = min(monthly_revenue_change)

    average_change = round((sum(monthly_revenue_change)/len(monthly_revenue_change)), 2)
        


print("Financial Analysis")        
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${high})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${low})")

output_file = os.path.join(".", "PyBank", "analysis", "pybank_results.text")
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_revenue}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${low})\n")