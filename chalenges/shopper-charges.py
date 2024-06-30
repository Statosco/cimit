totalPurchase = float(input("how much would you like to purchase: $"))
shipping = 0

if totalPurchase <= 50:
    shipping += 10
else:
    shipping = 0

total = totalPurchase + shipping

print(f"your total is ${total}")