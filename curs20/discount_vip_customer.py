def total_price(price, procent_discount):
    price_product = price - price * procent_discount / 100
    return price_product


def check_vip_status(cheltuieli):
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
    

sales = [102, 900, 1020, 2002, 3300, 1550, 250]
status_vip = check_vip_status(sales)

price_product = float(input("Introduceti pretul produsului: "))

if status_vip == True:
    discount_price_vip = 30
    price_vip = total_price(price_product, discount_price_vip)
    print(f"Pretul produsul pentru clientul VIP a fost redus de la {price_product} la {price_vip}")
else:
    discount_price_regular = 5
    price_regular = total_price(price_product, discount_price_regular)
    print(f"Pretul produsul pentru client a fost redus de la {price_product} la {price_regular}")
