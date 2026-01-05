daily_sales = [100, 200, 7887, 8990, 300, 678, 400, 1900, 500]
total_sales = 0
for sale in daily_sales:
    if sale < 200:
        print("Sale is too low, skipping: ", sale)
        continue
    elif sale > 5000:
        print("Suspicious! Sale is too high: ", sale, ". Stopping processing....")
        break
    total_sales += sale
    
print("Total sales:", total_sales)
# The code above calculates the total sales from a list of daily sales.