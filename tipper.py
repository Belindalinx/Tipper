price=int(input("\nHow much is your "+food_3+" today?"))
price_15=int(price)*15/100
price_20=int(price)*20/100

print("\nTips for 15 % is",price_15)
print("Total price with 15 % tips is",price+price_15)

print("\nTips for 20 % is",price_20)
print("Total price with 20 % tips is",price+price_20)

input("\nEnter to keep going")