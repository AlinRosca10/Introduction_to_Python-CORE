def total_price(price, procent_discount):
    price_product = price - price * procent_discount / 100
    return price_product


price_product_demo = 1000
procent_discount_demo = 40
mesaj = total_price(price_product_demo, procent_discount_demo)
print(f"Pretul produsului aflat la reducere este: {mesaj}")

list_product = ["phone", "smartTV", "headpods", "router", "magasin"]
list_phone_price = [10021, 2232, 2323, 1112, 9000, 1000]
list_smartTV_price = [1231, 1231, 2322, 3242, 3222, 3243]
list_headpods_price = [121, 2232, 2323, 1112, 9000, 1000]
list_router_price = [2231, 11231, 2322, 242, 3222, 3243]
list_magasin_price = [10021, 2232, 12323, 1112, 9090, 1200]

club_member = ["Alin", "Maria", "Alexa", "Dina", "Amalia", "Mira", "Doina"]
club_member_gold = ["Alin", "Dina", "Amalia", "Mira", "Doina"]
club_member_platinum = ["Alin", "Dina", "Mira"]
club_member_diamond = ["Alin", "Mira"]

client = input("Introduceti numele clientului: ")

if client in club_member_diamond:
    print("Clientul face parte din clubul de membri diamond!")
    discount_phone = 35
    discount_smartTV = 25
    discount_headpods = 23
    discount_router = 22
    discount_magasin = 30
    
elif client in club_member_platinum:
    print("Clientul face parte din clubul de membri platinum!")
    discount_phone = 30
    discount_smartTV = 20
    discount_headpods = 18
    discount_router = 17
    discount_magasin = 25
    
elif client in club_member_gold:
    print("Clientul face parte din clubul de membri gold!")
    discount_phone = 25
    discount_smartTV = 15
    discount_headpods = 13
    discount_router = 12
    discount_magasin = 20
    
elif client in club_member:
    print("Clientul face parte din clubul de membri!")
    discount_phone = 20
    discount_smartTV = 10
    discount_headpods = 8
    discount_router = 7
    discount_magasin = 15
    
else:
    print("Clientul nu face parte din clubul de membri!")
    discount_phone = 20
    discount_smartTV = 10
    discount_headpods = 8
    discount_router = 7
    discount_magasin = 15

for price in list_phone_price:
    mesage_phone = total_price(price, discount_phone)
    print(f"Pretul telefonului a fost redus de la {price} la {mesage_phone}")

for price in list_smartTV_price:
    mesage_smartTV = total_price(price, discount_smartTV)
    print(f"Pretul televizoarelor smart a fost redus de la {price} la {mesage_smartTV}")

for price in list_headpods_price:
    mesage_headpods = total_price(price, discount_headpods)
    print(f"Pretul castilor bluedhoth a fost redus de la {price} la {mesage_headpods}")

for price in list_router_price:
    mesage_router = total_price(price, discount_router)
    print(f"Pretul routerelor a fost redus de la {price} la {mesage_router}")
    
for price in list_magasin_price:
    mesage_magasin = total_price(price, discount_magasin)
    print(f"Pretul revistelor a fost redus de la {price} la {mesage_magasin}")