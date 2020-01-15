# Filname:tryexception.py

re = iter(range(5))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end ', i

print 'hahahaha'

#完整的结构

try:
    print "try"
except exception1:
    print 'except exception1'
except exception2:
    print 'except exception2'
except:
    print 'except'
else:
    print 'else'
finally:
    print 'finally'

try:
    print(a*2)
except TypeError:
    print('TypeError')
except:
    print('Not Type Error & Error noted')



def test_func():
    try:
        m = 1 / 0
    except NameError:
        print('Catch NameError in the sub-function')
try:
    test_func()
except ZeroDivisionError:
    print('Catch error in the main program.')

print 'hahhaaha'
try:
    raise StopIteration
except:
    print 'raise StopIteration'
print 'HHHHHHaaa'
