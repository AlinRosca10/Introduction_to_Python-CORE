def total_amount(cheltuieli):
    amount = 0
    for cheltuiala in cheltuieli:
        amount += cheltuiala
     
    if amount > 12500:
        return "Diamond"
    elif amount > 10000:
        return "Platinum"
    elif amount > 7500:
        return "Gold"
    elif amount > 5000:
        return "Regular"
    else:
        return False


sale = [23000, 200, 230, 300]
status_vip = total_amount(sale)
print(f"Statusul clientului este VIP: {status_vip}")