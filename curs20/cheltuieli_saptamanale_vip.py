def total_amount(cheltuieli):
    amount = 0
    for cheltuiala in cheltuieli:
        amount += cheltuiala

    if amount > 2500:
        return True
    else:
        return False
    
    
sale = [230, 200, 230, 300]
status_vip = total_amount(sale)
print(f"Statusul clientului este VIP: {status_vip}")