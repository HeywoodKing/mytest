# Filename:dict.py

# �����ֵ�
ab = {"user1" : "user1@test.com", "user2" : "user2@test.com"}

# ����
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))

# �������
if not "tom" in ab: # or not ab.has_key("tom")
    ab["Tom"] = "tom@test.com"

# ����
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))

# ����
print("user1's address is %s" % ab["user1"])

# ɾ��
del ab["Tom"]

# ����
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))


