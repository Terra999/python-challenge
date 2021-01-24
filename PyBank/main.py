# Huge thanks to Sharon Templin for helping me with the code for the monthly change calculation and how to move past the first row
# Huge thanks to TA Benji for helping me with calculating the greatest increase and decrease of the monthly change.

# Import os module
import os

# Import csv module
import csv

# Find file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

# Open and read csv
with open(csvpath) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Identify variables
    total_months = 0
    total_revenue = 0
    current_row = 0
    prior_row = 0
    total_change = 0
    first_loop = True
    monthly_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    month = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    
    # Begin for loop
    for row in budget_csv:

        # Calculate total months
        total_months = total_months + 1
    

        # Find the net total amount of Profit/Losses
        total_revenue = total_revenue + int(row[1])


        # Calculate the changes in "Profit/Losses" over the entire period
        current_row = int(row[1])
        # print(current_row)

        # To compensate for the blank first row set to False
        if first_loop == False:
            monthly_change = current_row - prior_row
          
            # Calculate greatest monthly increase along with the month it occurred in
            if greatest_increase < monthly_change:
                greatest_increase = monthly_change
                greatest_increase_month = row[0]

            # Calculate greatest monthly decrease along with the month it occurred in
            if greatest_decrease > monthly_change:
                greatest_decrease = monthly_change
                greatest_decrease_month = row[0]


        # Starting point after moving past the blank row       
        prior_row = current_row


        # Find sum of total changes
        total_change = total_change + monthly_change
        # print(total_change)

        first_loop = False
    
    # Now calculating the average of the monthly change
    average_monthly_change = round(total_change/(total_months - 1), 2)
    # print(average_monthly_change)

print(" ")
print("Financial Analysis")       
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease})")


 # Specify the file to write to
output_path = os.path.join("Analysis", "PyBank.txt")

# # Open the file using "write" mode. Specify the variable to hold the content.
with open(output_path, "w") as text:

    print(" ", file = text)
    print("Financial Analysis", file = text)       
    print("---------------------------------", file = text)
    print(f"Total Months: {total_months}", file = text)
    print(f"Total: ${total_revenue}", file = text)
    print(f"Average Change: ${average_monthly_change}", file = text)
    print(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase})", file = text)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease})", file = text)
