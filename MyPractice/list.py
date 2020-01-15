# Filename:list.py

# ´´½¨
shoplist = ['apple', 'mango', 'tomato', 'carrot', 'banana']
print("I have", len(shoplist), "items to purchase.")

# ±éÀú
for item in shoplist:
    print(item)

# Ìí¼Ó
print("I also have to buy rice.")
shoplist.append("rice")
print("My shopping list is now", shoplist)

# ÅÅÐò
shoplist.sort()
print("Sorted shopping list is", shoplist)

# ¼ìË÷
print("The first item I will buy is", shoplist[1])

# É¾³ý
olditem = shoplist[1];
del shoplist[1]
print("I bought the", olditem)
print("My shopping list is now", shoplist)



