# Filename:list.py

# ����
shoplist = ['apple', 'mango', 'tomato', 'carrot', 'banana']
print("I have", len(shoplist), "items to purchase.")

# ����
for item in shoplist:
    print(item)

# ���
print("I also have to buy rice.")
shoplist.append("rice")
print("My shopping list is now", shoplist)

# ����
shoplist.sort()
print("Sorted shopping list is", shoplist)

# ����
print("The first item I will buy is", shoplist[1])

# ɾ��
olditem = shoplist[1];
del shoplist[1]
print("I bought the", olditem)
print("My shopping list is now", shoplist)



