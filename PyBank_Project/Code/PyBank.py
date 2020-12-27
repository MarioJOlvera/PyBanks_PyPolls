import csv
import os

file_to_load = os.path.join("Resources", "Budget_Data.csv")
file_to_output = os.path.join("Analysis", "Budget_Analysis.txt")

# Track financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header now
    header = next(reader)

    # Extract first row to avoid appending net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greates decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"--------------------\n"
    f"TOTAL MONTHS: {total_months}\n"
    f"TOTAL: ${total_net}\n"
    f"AVG CHANGE: ${net_monthly_avg:.2f}\n"
    f"GREATEST INCREASE IN PROFITS: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"GREATEST DECREASE IN PROFITS: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)



