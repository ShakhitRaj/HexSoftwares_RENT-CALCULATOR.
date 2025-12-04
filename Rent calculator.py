# Python project (Rent calculator)
# person 3
# total rent
# Food charges
# Water Charges
# Electricity charges

total_rent = int(input("Enter the total rent =" ))
food = int(input("Enter the total food charges =" ))
water = int(input("Enter the total water charges =" ))
elec_Charges = int(input("Enter the total electricity charges =" ))
person = int(input("Enter the number of person living in room =" ))

total_Amount = (total_rent + food +elec_Charges) // person
print("Each person will pay =", total_Amount)
