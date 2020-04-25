# import the os module. 
import os
# module for csv files
import csv

# set varibles

total = 0
profit_losses = 0
greatest_date = ''
greatest_increase = 0
greatest_decrease = 999999999
greatest_loss_date = ''
previousrow = 0
changelist = []
difference = []

# next need a path to file- open git in same folder
csvpath = os.path.join('Resources', 'budget_data.csv')
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    firstrow = next(csvreader)
    # loop should start in second row now
    for row in csvreader:

        #print(row) in this example total records

        total = total + 1
        profit_losses = profit_losses + int(row[1])
           # doing the math for current value of a row vs previous row value
        currentdifference = int(row[1])-previousrow
        #adding to end of list
        difference.append(currentdifference)


        # were checking if current profit is greater than next one
        if int(row[1]) > greatest_increase and total > 1:
         
                    
            if currentdifference > greatest_increase:
                greatest_increase = currentdifference
                greatest_date = row[0]
        # were checking if current profit loss is greater than the next one      
        if int(row[1]) < greatest_decrease and total > 1:
                   
            if currentdifference < greatest_decrease:
                greatest_decrease = currentdifference
                greatest_loss_date = row[0] 

        previousrow = int(row[1])

        

        # this is where the file will write to
output_path = os.path.join("Analysis", "HomeworkPyBank.txt")

        # open file in write mode. 
        # copy what you print to terminal 
        # after the word print to the end of txtfile.write
with open (output_path, 'w') as txtfile: 
    
    txtfile.write("\nFinancial Analysis")
    txtfile.write("\n-------------------------------")
    txtfile.write("\ntotal months " + str(total))
    txtfile.write("\nprofit losses " + str(profit_losses))
    txtfile.write("\nGreatest increase in profits " + str(greatest_increase ))
    txtfile.write("\nMonth of Greatest profit " + str(greatest_date))
    txtfile.write("\nGreatest decrease in Profits " + str(greatest_decrease) )
    txtfile.write("\nMonth of Greatest Decrease " + str(greatest_loss_date))

     
# #spaced the print down for easier reading on the terminal
print("                  ")
print("Financial Analysis")
print("-------------------------------")
print("total months " + str(total))
print("profit losses " + str(profit_losses))
print("Greatest increase in profits: " + str(greatest_increase ))
print("Month of Greatest Profits: " + str(greatest_date))
print("Greatest Decrease in Profits: " + str(greatest_decrease))
print("Month of Greatest Decrease: " + str(greatest_loss_date))
total_difference = 0

for dif in difference:
    total_difference =total_difference + dif

Average_change = (total_difference / total - 1 )

print("Average Change: " + str(Average_change))







 



