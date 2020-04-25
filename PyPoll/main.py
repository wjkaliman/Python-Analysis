#import the os 
import os
import csv

# set varible
total = 0
Candidates = []
Unique_Candidates = []
results = {}




csvpath = os.path.join('Resources', 'election_data.csv')
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    firstrow = next(csvreader)
    # loop should start in second row now
    for row in csvreader: 
        total = total + 1
        #append is adding the value of row/column 2 down the list counting all names
        Candidates.append(row[2])  
        #add unique candiates to the unique candidates list
        if row[2]not in Unique_Candidates:
            Unique_Candidates.append(row[2])

    #for each unique candidate 
    # loop thru candidates and count each time the candidate appears
    for Candidate in Unique_Candidates:

        results[Candidate] = Candidates.count(Candidate)
# this needs to be here because results from code is above    
Keymax = max(results, key=results.get) 

# this is where the file will write to
output_path = os.path.join("Analysis", "HomeworkPyPoll")
       # open file to write 
with open (output_path, 'w') as txtfile:
    txtfile.write("\nelection Results")
    txtfile.write("\n----------------------------")
    txtfile.write("\ntotal votes: " + str(total))
    txtfile.write("\n----------------------------")
   
    #thank you to geekforgeeks.com for this code!
    #txtfile.write("\n(f"{k}: {format(v/total,'%')} ({v})") ")
    for k, v in results.items():    
        txtfile.write("\n" + str(k) + " " + (format(v/total,'%') + " " + str(v) ))
    txtfile.write("\n----------------------------")
    txtfile.write("\nWinner: " +(Keymax))

#spaced the print down for easier reading on the terminal
print("                ")    
print("Election Results")
print("-----------------------------------")
print("total Votes: " + str(total))
print("-----------------------------------")
#for each row in the results dictionary print key and value
#key is cnadidate-value is the total votes- total/v gives %
for k, v in results.items():
    print(f"{k}: {format(v/total,'%')} ({v})")

# display winner based on popular votes    
print("-----------------------------------")
print("Winner:" +(Keymax))






