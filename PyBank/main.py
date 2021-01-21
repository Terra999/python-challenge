# Import os module
import os

# Import csv module
import csv

# Find file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)



# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Identify variables
    total_months = 0
    revenue = []
    months = []
    total_revenue = 0
    net_total = 0
    current_row = 0
    prior_row = 0
    total_change = 0
    first_loop = True
    monthly_change = 0
    
    # Begin for loop
    for row in csvreader:

        total_months = total_months + 1


    
        # Put revenue in list
        # revenue.append(row[1])
        # print(revenue)

        # Find the net total amount of Profit/Losses
        total_revenue = total_revenue + int(row[1])
        

        # Calculate the changes in "Profit/Losses" over the entire period
        current_row = int(row[1])
        # print(current_row)

        if first_loop == False:
            monthly_change = current_row - prior_row
            # Print monthly change
            # print(f"Monthly Change: {monthly_change}")
        
                
        prior_row = current_row

        # Find sum of total changes
        total_change = total_change + monthly_change
        # print(total_change)

        first_loop = False
    
    # Now calculating the average of the monthly change
    average_monthly_change = round(total_change/(total_months - 1), 2)
    # print(average_monthly_change)





    # Find total number of months included in dataset
    # total_months = len(list(csvreader)) + 1
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_revenue}")
    print(f"Average Change: ${average_monthly_change}")







         
