import csv
import os


data_file =os.path.join('Resources', 'election_data.csv')

#lists/variables
voter_ID=[]
candidates=[]
unique_candidates=[]
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

with open (data_file, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader, None)

    
    for row in csvreader:
        #fill empy list with voter ID 
        voter_ID.append(row[0])
        

        #total number of votes cast
        total_votes =len(voter_ID)    

        #unique candidates, append to unique candidates list
        unique_cand=set(candidates)
        unique_candidates.append(unique_cand)


        #total number of votes per candidate
        if row[2]== "Khan":
         khan_votes += 1
        elif row[2]=="Correy":
         correy_votes += 1
        elif row[2]== "Li":
         li_votes+= 1
        else:
         otooley_votes+= 1


#make dictionary to find winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Zip the list of candidate(key) and the total votes(value)
candidates_votes = dict(zip(candidates,votes))
key = max(candidates_votes, key=candidates_votes.get)

#percentage each candidate won
khan_percent= (khan_votes/total_votes) * 100
correy_percent=(correy_votes/total_votes) * 100
li_percent=(li_votes/total_votes) * 100
otooley_percent= (otooley_votes/total_votes) * 100

# Show output
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"--------------------------")
print(f"Winner: {key}")
print(f"--------------------------")

output_file=os.path.join('pypoll', 'pypoll.txt')


with open('pypoll.txt', 'w') as text:
    
    text.write(f"Election Analysis" + "\n")
    text.write(f"-------------------------\n\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write(f"-------------------------" + "\n")
    text.write(f"Khan: {khan_percent:.3f}% ({khan_votes})"+ "\n")
    text.write(f"Correy: {correy_percent:.3f}% ({correy_votes})"+ "\n")
    text.write(f"Li: {li_percent:.3f}% ({li_votes})" + "\n")
    text.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})" + "\n")
    text.write(f"---------------------------"+ "\n")
    text.write(f"Winner: {key}" + "\n")
    text.write(f"---------------------------")

#opens the output and prints
with open(output_file, 'r') as readfile:
   print(readfile.read())







        
        

