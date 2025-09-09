# input value of items user want to buy
price = float(input("How much did you buy?($) "))

# calculate final prices after discount
if price >= 5000:
    final_price = price - (price * 0.2)
    print(f"Price after 20% discount: ${final_price}")
elif 5000 > price >= 2000:
    final_price = price - (price * 0.1)
    print(f"Price after 10% discount: ${final_price}")
elif 2000 > price:
    final_price = price
    print(f"Price without discount: ${final_price}")
else:
    print("Invalid price")