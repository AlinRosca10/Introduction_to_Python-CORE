all_member = ["Alexander", "John", "Michael", "Sarah", "Jessica", "Emily", 
              "David", "Sophia", "Daniel", "Olivia"]
loyalty_member = ["John", "Sarah", "Jessica", "Emily", "David", "Sophia"]

for member in all_member:
    if member not in loyalty_member:
        print(f"{member} is not a loyalty member.")
    else:
        print(f"{member} is a loyalty member.")
