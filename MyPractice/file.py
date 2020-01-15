# Filename:file.py

f = open("test.txt", "r")
content = f.read(10)
print content
#f.write('I like apple')
print content
content = f.readline()
print content
content = f.readlines()
print content
f.close()

