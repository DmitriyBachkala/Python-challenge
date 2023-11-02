import csv

# Define file paths
# Input
input_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyBank/Resources/budget_data.csv"

# Output
output_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyBank/Analysis/financial_analysis.txt"

# New variables to store financial data
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(input_file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract data from each row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss

        # Calculate changes in "Profit/Losses"
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)

        # Store the current "Profit/Loss" for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = round(sum(profit_loss_changes) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Generate the financial analysis report
financial_analysis = f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${net_total}\nAverage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"

# Print the analysis to the terminal
print("")
print(financial_analysis)
print("")

# Export the results to the specified output file
with open(output_file_path, 'w') as file:
    file.write(financial_analysis)