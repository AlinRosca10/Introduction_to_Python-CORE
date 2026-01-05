campaign_days = 0
max_days = 30
campaign_terminated = False

print("Welcome to the promotion campaign!")
while campaign_days < max_days and not campaign_terminated:
    campaign_days += 1
    sales = int(input(f"Enter the sales for day {campaign_days}: "))
    budget = int(input(f"Enter the budget for day {campaign_days}: "))
    
    if sales >= 50 and sales <= 100 and budget < 1000:
        print("This was a good day!")
    elif sales > 100 and budget > 2000:
        print("Warning!")
        campaign_terminated = True
    else:
        print("Regular day!")
        
