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






tot_mths = len(lst_month)
grand_tot_pl=sum(lst_pl)
avg_chng=average(avg_delta)
print(header)
print(lst_month)
print(lst_pl)
print("total Months :" + str(tot_mths))
print("Total Profit/loss :" + str(grand_tot_pl))
print("Average change between months : "+ str(round(avg_chng,2)))