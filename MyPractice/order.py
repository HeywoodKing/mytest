# Filename:order.py

shoplist = ["apple", "mango", "carrot", "orange", "banana", "peanut"]

# ����
# ����������
print("Item 0 is", shoplist[0])
print("Item -1 is", shoplist[-1])
print("Item -2 is", shoplist[-2])

# ��Ƭ������
print("Item 1 to 3 is", shoplist[1:3])
print("Item 2 to end is", shoplist[2:])
print("Item start to end is", shoplist[:])

name = "known"
print("charactor 1 to 3 is", name[1:3])

# ����ͬ�������Ǹ�����������������£�λ���Ǵ�����β��ʼ����ġ�
# ��ˣ�shoplist[-1]��ʾ���е����һ��Ԫ�ض�shoplist[-2]ץȡ���еĵ����ڶ�����Ŀ

# ��Ƭ�����������������һ�������ţ�����������һ�Կ�ѡ�����֣�����ð�ŷָ
# ע��������ʹ�õ�����������ʮ�����ơ���ס���ǿ�ѡ�ģ���ð���Ǳ����

# ��Ƭ�������еĵ�һ������ð��֮ǰ����ʾ��Ƭ��ʼ��λ�ã�
# �ڶ�������ð��֮�󣩱�ʾ��Ƭ����������������ָ����һ������
# Python�ʹ������׿�ʼ�����û��ָ���ڶ���������Python��ֹͣ������β��
# ע�⣬���ص����дӿ�ʼλ�� ��ʼ ���պ��� ���� λ��֮ǰ������
# ����ʼλ���ǰ�����������Ƭ�еģ�������λ�ñ��ų�����Ƭ�⡣

# ����������
print("Simple Assignment")
mylist = shoplist

del shoplist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)

print("Copy by making a full slice")
mylist = shoplist[:]
print("shoplist is", shoplist)
print("mylist is", mylist)

# �ַ�������
name = "Swaroop"
if name.startswith("Swa"):
    print("Yes, the string starts with 'Swa'")

if "a" in name:
    print("Yes, it contains the string 'a'")

if name.find("war") != -1:
    print("Yes, it contains the string 'war'")

delimiter = "-*-"
mylist = ["Brazil", "Russia", "India", "China"]
print(delimiter.join(mylist))




