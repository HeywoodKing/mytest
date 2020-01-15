# Filename:contextmanager.py

f = open('new.txt','w')
print(f.closed)
f.write('Hello wrold!')
f.close()
print(f.closed)

with open('new.txt','w') as f:
    print(dir(f))
    print(f.closed)
    f.write('Hello World!')
print(f.closed)

class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = 'I say:' + self.text
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text + "!"

with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)


#VAR = EXPR
#VAR = VAR.__enter__()
#try:
#    pass
#finally:
#    VAR.__exit__()
