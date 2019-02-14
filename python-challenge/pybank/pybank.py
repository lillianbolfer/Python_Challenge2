
import csv
import os


data_file =os.path.join('Resources', 'budget_data.csv')


with open (data_file) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    #lists 
    months =[]
    profits_losses = []
    

    for row in csvreader:
        #fill empy lists with months and revenue data from file
        months.append(row[0])
        profits_losses.append(int(row[1]))


    #total number of month in data set
    total_months = len(months)

     #variables
    net_total_profits=0 #total of profits and losses
    greatestInc_prof=profits_losses[0]
    greatestDec_prof=profits_losses[0]

    #find greatest increase and decrease in a particular month
    for i in range(len(profits_losses)):
        if profits_losses[i] >= greatestInc_prof:
            greatestInc_prof = profits_losses[i]
            increase_month = months[i]
        elif profits_losses[i] <= greatestDec_prof:
            greatestDec_prof = profits_losses[i]
            decrease_month = months[i]

       #the net revenue of the data set equals the combination of profits and losses across i
        net_total_profits += profits_losses[i]

#average change of revenue across data set
average_change= (net_total_profits/total_months)

output_file=os.path.join('pybank', 'pybank.txt')


with open('pybank.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(net_total_profits) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatestInc_prof) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatestDec_prof) + ")\n")
    text.write("----------------------------------------------------------\n")

#opens the output and prints
with open(output_file, 'r') as readfile:
   print(readfile.read())











