shop_list = []
while True:
    item = input("What do you want to buy? (type 'done' to finish): ")
    if item.lower() == "done":
        break
    shop_list.append(item)

print("Your shopping list:")
for thing in shop_list:
    print("-", thing)
