no_customers_jan = 1200
no_customers_feb = 950
no_customers_mar = 1300

avg_jan = 58.75
avg_feb = 47.50
avg_mar = 98.25

expenses_mar = 4000

total_customers = no_customers_jan
print("Total number of customers: ", total_customers)

#   total_customers = no_customers_jan + no_customers_feb
print("Total number of customers: ", total_customers)

total_customers += no_customers_feb
print("Total number of customers: ", total_customers)

total_customers += no_customers_mar
print("Total number of customers: ", total_customers)

total_avg = avg_jan + avg_feb
print("Total average: ", total_avg)

total_avg += ((avg_mar * 31) - expenses_mar) / 31
print("Total average: ", total_avg)

total_avg /= 3
print("Total average: ", total_avg)

total_avg += avg_mar
print("Total average: ", total_avg)

total_avg /= 4
print("Total average: ", total_avg)
