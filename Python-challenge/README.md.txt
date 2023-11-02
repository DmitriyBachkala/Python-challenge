PyBank
-
When in came to the input path and output path i use chat.openai.com to assit me in specifying the correct paths

input_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyBank/Resources/budget_data.csv"
output_file_path = "C:/Users/golde/OneDrive/Desktop/Data Analyst/Data Analysis Projects/assignments & projects/Python-challenge/PyBank/Analysis/financial_analysis.txt"
-
used chat.openai.com to get the correct code for calculating the total amout of profits and losses, and to calculate the changes in proffit and losses

 net_total += profit_loss

        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)
-
used chat.openai.com to correct the code to build the report

financial_analysis = f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${net_total}\nAverage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
-



PyPoll
-
Code for calculating the count for each candidate from chat.openai.com

 # Calculate the total number of votes
        total_votes += 1

        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
-
used chat.openai.com to correct the code to build report

election_results = f"Election Results\n{'-' * 25}\nTotal Votes: {total_votes}\n{'-' * 25}\n"

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    election_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

election_results += f"{'-' * 25}\nWinner: {winner}\n{'-' * 25}"
-