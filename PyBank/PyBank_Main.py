import csv
import os


file_num = 2


file = os.path.join('raw_data', 'budget_data_'+ str(file_num) +'.csv')


months = []
revenue = []


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))


total_months = len(months)


greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0


for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]


average_change = round(total_revenue/total_months, 2)


output_dest = os.path.join('output_data','pybank_output_' + str(file_num) + '.txt')


with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')


with open(output_dest, 'r') as readfile:
    print(readfile.read())