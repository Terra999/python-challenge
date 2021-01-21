import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
revenue = []
total_revenue = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        # Add list for month
        month.append(row[0])
        # print(month)

        # Add list for revenue
        revenue.append(row[1])
        print(revenue)

       # Find total number of months included in dataset
        total_months = len(list(csvreader))
        print(f"Total Months: {total_months}")

        total_revenue = (row[1])
        print(total_revenue)