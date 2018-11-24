import os
import csv
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

print("Li got : " + str('{:,.2%}'.format(li/totalvotes)+" " +str(li)))
print("Khan got : " + str('{:,.2%}'.format(khan/totalvotes)+" "  + str(khan)))
print("Correy got : " + str('{:,.2%}'.format(correy/totalvotes)+" " + str(correy)))
print("O'Tooley got : " +  str('{:,.2%}'.format(tooley/totalvotes)+" " +  str(tooley)))
#print('Total Votes : ' + str(totalvotes))
print("---------------------------------------------------"
#print("==================================================")
#print(candidate_res)
sorted_candidate_res=sorted(candidate_res.items(),key=lambda cv:(cv[1],cv[0]))
#print(sorted_candidate_res[-1])
winnerlist=sorted_candidate_res[-1]

print("Winner: " + winnerlist[0])
print("---------------------------------------------------")