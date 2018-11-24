import os
import csv
final_header =["Total Votes","Khan","Correy","Li","O'Tooley","Winner"]
percentage_votes=[]
final_votes=[]
value=0
khan = 0
tooley=0
li=0
correy=0
candidt=''
candidate_res={"Li":0,"Khan":0,"Correy":0,"O'Tooley":0}
voters=[]
sorted_candidate_res={}
totalvotes=0
winnerlist=[]
voter_csv = os.path.join("election_data.csv")
with open(voter_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    #header=next(csvreader)
    for row in csvreader:
        for key,value in row.items():
           # print(key,value)
            if key =="Candidate":
                candidt=value
                if candidt=="Li":
                    li+=1
                    candidate_res[candidt]=li
                elif candidt=="Khan":
                    khan+=1
                    candidate_res[candidt]=khan
                elif candidt=="Correy":
                    correy+=1
                    candidate_res[candidt]=correy
                else:
                    tooley+=1
                    candidate_res[candidt]=tooley
totalvotes=li+khan+correy+tooley



print("Election Results")
print("---------------------------------------------------")
print("Total Votes : " + str(totalvotes))
print("---------------------------------------------------")
print("Khan : " + str('{:,.2%}'.format(khan/totalvotes)+" "  + str(khan)))
print("Correy : " + str('{:,.2%}'.format(correy/totalvotes)+" " + str(correy)))
print("Li : " + str('{:,.2%}'.format(li/totalvotes)+" " +str(li)))
print("O'Tooley : " +  str('{:,.2%}'.format(tooley/totalvotes)+" " +  str(tooley)))
#print('Total Votes : ' + str(totalvotes))
print("---------------------------------------------------")
#print("==================================================")
#print(candidate_res)
sorted_candidate_res=sorted(candidate_res.items(),key=lambda cv:(cv[1],cv[0]),reverse=True)
#print(sorted_candidate_res)
#print(sorted_candidate_res[-1])
winnerlist=sorted_candidate_res[0]

print("Winner: " + winnerlist[0])
print("---------------------------------------------------")
percentage_votes.append("")
final_votes.append(totalvotes)
for value in sorted_candidate_res:

    final_votes.append(value[1])
    calc_per='{:,.2%}'.format(value[1]/totalvotes)
    percentage_votes.append(calc_per)
percentage_votes.append(winnerlist[0])
final_votes.append("")

result=zip(final_header,percentage_votes,final_votes)
#print(result)
# Set variable for output file
output_file = os.path.join("Election_Analysis.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Election Analysis"])
    writer.writerow(["-------------------------------------------------------"])
    # Write in zipped rows
    writer.writerows(result)