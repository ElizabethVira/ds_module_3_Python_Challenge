# Conect the CVS file to able to read the content
# Total number of months
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# Module for reading CSV files and set path for file

import csv
csvpath = "PyBank/Resources/budget_data.csv"

# Create the variables
month_total = 0
total_profit = 0

# For changes over period
last_month_profit = 0
period_changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding (previus classes code)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (previus classes code)
    csv_header = next(csvreader)

    for row in csvreader:

        # Total months count
        month_total += + 1

        # Add profit
        total_profit += + + int(row[1])

        # Calulate last month profit and subtract from actual month profit
        # Append that change to the list

        if(month_total == 1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            period_changes.append(change)
            month_changes.append(row[0])

            # Reset last month profit when calculating the next row
            last_month_profit = int(row[1])

    avg_change = sum(period_changes) / len(period_changes)

    max_change = max(period_changes)
    max_month_indx = period_changes.index(max_change)
    max_month = month_changes[max_month_indx]

    min_change = min(period_changes)
    min_month_indx = period_changes.index(min_change)
    min_month = month_changes[min_month_indx]

# Print Financial Analysis results
output = (    

    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: {avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})\n"
)
print(output)

# Creating a text file
with(open("output_PyBank.txt", "w") as f):
    f.write(output)

