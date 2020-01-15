# Filename:dict.py

# 创建字典
ab = {"user1" : "user1@test.com", "user2" : "user2@test.com"}

# 遍历
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))

# 添加数据
if not "tom" in ab: # or not ab.has_key("tom")
    ab["Tom"] = "tom@test.com"

# 遍历
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))

# 检索
print("user1's address is %s" % ab["user1"])

# 删除
del ab["Tom"]

# 遍历
for name, address in ab.items():
    print("Contact %s at %s" % (name, address))


