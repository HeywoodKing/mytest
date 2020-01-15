# Filename:dictdemo2.py

dict = {"lilei":60, "lisi":80, 'sam':95, 'tom':99}

for key in dict:
    print dict[key]
    
for key in dict.keys():
    print key
    
for val in dict.values():
    print val

for item in dict.items():
    print item

for item in dict.items():
    print item[1]
    
print(len(dict))

del dict['lisi']
print(len(dict))

dict.clear()
print(len(dict))
