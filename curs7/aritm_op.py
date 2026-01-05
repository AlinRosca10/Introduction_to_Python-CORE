no_custumers_jan = 1200
no_custumers_feb = 1500
no_custumers_mar = 1800
no_custumers_apr = 2000
no_custumers_may = 2500
no_custumers_jun = 3000

total_custumers = no_custumers_jan+no_custumers_feb+no_custumers_mar+no_custumers_apr+no_custumers_may+no_custumers_jun
print("Total number of custumers in the first half 7 of the year: ", total_custumers)
print("Average number of custumers in the first half of the year: ", total_custumers / 6)
jan_amount = 1200*10.5
feb_amount = 1500*10.5
mar_amount = 1800*10.5
apr_amount = 2000*10.5
may_amount = 2500*10.5

days_no_jan = 31
days_no_feb = 28

avg_income_jan = jan_amount / days_no_jan
avg_income_feb = feb_amount / days_no_feb

print("Average income in January: ", avg_income_jan)
print(type(avg_income_jan))
print("Average income in February: ", avg_income_feb)
print(type(avg_income_feb))

items_no = 100
employes_no = 35

no_items_per_employe = items_no / employes_no
print("Number of items per employe: ", no_items_per_employe)
print(type(no_items_per_employe))

no_items_per_employe_left = items_no%employes_no
print("Number of items per employe left: ", no_items_per_employe_left)
print(type(no_items_per_employe_left))

no_custumers_jan = 1200
no_customers_feb = 950

total_custumers = no_custumers_jan + no_custumers_feb
print("Total numbers of custumers: ", total_custumers)
no_mounts = 2
avg_custumers = total_custumers / no_mounts
print("Average numbers of custumers: ", avg_custumers)