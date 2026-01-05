customers_jan = 1200
avg_feb = 52.75
customers_feb = 950

ans = customers_jan > 100 and customers_feb > 500 \
    and avg_feb > 100
print(ans)
print(type(ans))

ans = customers_jan > 100 or customers_feb > 500 \
    or avg_feb > 100
print(ans)
print(type(ans))

ans = not (customers_jan > 100)
ans2 = customers_jan <= 100
print(ans)
print(ans2)
print(type(ans))
print(type(ans2))

ans = customers_jan != 1200
print(ans)

ans = not (customers_jan == 1200)
print(ans)

no_custumers_jan = 155
no_custumers_feb = 120
no_custumers_mar = 155

avg_jan = 58
avg_feb = 47.50
avg_mar = 58

ans = no_custumers_jan > no_custumers_feb
print("Number of customers in January is greater than in February: ", ans)

ans = avg_jan < avg_feb
print("Average in January is smaller than in February: ", ans)
print(type(ans))

ans1 = no_custumers_mar > 150 or avg_mar > 60
print("Number of customers in March is greater than 150 or average in March is greater than 60: ", ans1)
print(type(ans1))

ans2 = not (no_custumers_mar < 100)
print("Number of customers in March is not smaller than 100: ", ans2)
print(type(ans2))
