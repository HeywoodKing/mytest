# Filename:zoo

# Ԫ�� Ԫ����б�ʮ�����ƣ�ֻ����Ԫ���ǲ����Ըı�ģ������ܱ��޸�
# Ԫ������һ��Բ����()��ʾ��ÿ������֮��Ҳ���ö��Ÿ�����
# Ԫ��ͨ������ʹ�����û�����ĺ����ܹ���ȫ�ز���һ��ֵ��ʱ��
# ����ʹ�õ�Ԫ���ֵ����ı䡣
zoo = ("wolf", "elephant", "penguin")
print("Number of animals in the zoo is",len(zoo))

new_zoo = ("monkey", "dolphin", zoo)
print("Number of animals in the new zoo is",len(new_zoo))

print("All animals in new zoo are", new_zoo)
print("Animals brought from old zoo are", new_zoo[2])
print("Last animal brought form old zoo is", new_zoo[2][2])

# Ԫ����ͨ�����÷������ڴ�ӡ����С�
age = 22
name = "Ching"
print("%s is %d years old" % (name, age))
print("Why is %s playing with that python?" % name)
