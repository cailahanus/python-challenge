
#First Import your csv file
import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

# the text below is within the script to replicate the results in the display images
print("Financial Analysis")
print("-----------------------")

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #The total number of months included in the dataset
    #Each row is a new month

    #The below is unneeded but prints the headers of the attached csv file
    csv_header = next(csvreader)
    #print(len(csv_header))

    # syntax below is to define the variables before beginning our loop
    total_months = 0
    total_profit = 0
    # creating a list so a new data set can be created and referenced
    total_net_changes = []
    max_changes = 0
    # below saves the date as a string
    max_changes_date = ''
    min_changes = 0
    min_changes_date =''

    
    for row in csvreader:

        #count each row of data after the header to obrain the total number of months
        total_months += 1

        profit_loss = int(row[1])
        
        # while counting the months, we are also keep the Profit/ Losses over the entire period
        total_profit += profit_loss   
        
        # referenced the hot days loop
        if total_months > 1:
            
            net_change = profit_loss - previous_profit_loss

            # below creates a list of data values for future analysis
            total_net_changes.append(net_change)

            # first loop for finding the max increase with corresponding date
            # loop through net changes until 
            if net_change > max_changes:

                max_changes = net_change
                
                # below saves the date in the same row as a string
                max_changes_date = row[0]
            
            # Now repeating to find the max decrease with corresponding date
            if net_change < min_changes:
                
                min_changes = net_change
                
                min_changes_date = row[0]
     
        previous_profit_loss = profit_loss

    # Now obtain the overall average change
    # average change is found by taking the net profits but the number of values 
    average_change = sum(total_net_changes)/len(total_net_changes)

    # the reference has the average change rounded to two decimal places
    # syntax found on ChatGPT
    round_average_change = round(average_change, 2)

    # Now print results to match the reference results
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round_average_change}")
    print(f"Greatest Increase in Profits: {max_changes_date} (${max_changes})")
    print(f"Greatest Decrease in Profits: {min_changes_date} (${min_changes})")
    #find total profit and losses