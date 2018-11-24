import os
import csv
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
budget_csv = os.path.join("budget_data.csv")
# Lists to store data
lst_month = []
lst_pl = []
header =[]
avg_delta=[]
sorted_deltas_pl=[]
grt_inc_month=""
grt_dec_month=""
grt_inc_pr_indx = 0
grt_dec_pr_indx = 0
grt_inc_pr_val = 0.0
grt_dec_pr_val = 0.0
tot_mths =0
grand_tot_pl = 0.0
indx=0
avg_chng=0.0
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        lst_month.append(row[0])
        lst_pl.append(float(row[1]))

for indx in range(1,len(lst_pl)) :
    avg_delta.append(float(lst_pl[indx])-float(lst_pl[indx-1]))
    #print(float(lst_pl[indx]))
    #print(float(lst_pl[indx-1]))
    #print(avg_delta)

sorted_deltas_pl=sorted(avg_delta,reverse=True)
print(sorted_deltas_pl)
grt_inc_pr_val = sorted_deltas_pl[0]
grt_dec_pr_val = sorted_deltas_pl[-1]
grt_inc_pr_indx = avg_delta.index(grt_inc_pr_val)
grt_dec_pr_indx = avg_delta.index(grt_dec_pr_val)
grt_inc_month=lst_month[grt_inc_pr_indx+1]
grt_dec_month=lst_month[grt_dec_pr_indx+1]

print(" Highest profit for the month of " +grt_inc_month+ " = " + str(grt_inc_pr_val) )
print(" Lowest profit for the month of " +grt_dec_month+ " = " + str(grt_dec_pr_val) )

tot_mths = len(lst_month)
grand_tot_pl=sum(lst_pl)
avg_chng=average(avg_delta)
print(header)
print(lst_month)
print(lst_pl)
print("total Months :" + str(tot_mths))
print("Total Profit/loss :" + str(grand_tot_pl))
print("Average change between months : "+ str(round(avg_chng,2)))