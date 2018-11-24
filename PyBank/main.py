import os
import csv

#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)




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
final_header =["Total Months","Total","Average  Change","Greatest Increase in Profits","Greatest Decrease in Profits"]
final_value=[]
dict_results={}
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


tot_mths = len(lst_month)
grand_tot_pl=sum(lst_pl)
avg_chng=average(avg_delta)
#print(header)
#print(lst_month)
#print(lst_pl)
print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: " + str(tot_mths))
print("Total: " + str('${:,.2f}'.format(grand_tot_pl,2)))
print("Average Change: "+ str('${:,.2f}'.format(avg_chng,2)))
print("Greatest Increase in Profits: " +grt_inc_month+ " (" + str('${:,.2f}'.format(grt_inc_pr_val,0))+")")
print("Greatest Decrease in Profits: " +grt_dec_month+ " (" + str('${:,.2f}'.format(grt_dec_pr_val,0))+")" )
final_value.append(tot_mths)
final_value.append('${:,.2f}'.format(grand_tot_pl,2))
final_value.append('${:,.2f}'.format(avg_chng,2))
final_value.append(grt_inc_month + " "+'${:,.2f}'.format(grt_inc_pr_val,0))
final_value.append(grt_dec_month + " "+ '${:,.2f}'.format(grt_dec_pr_val,0))
print("==================================================")
#print(final_header)
#print(final_value)
result=zip(final_header,final_value)
#print(result)

output_file = os.path.join("Financial_Analysis.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------------------------------"])

    writer.writerows(result)