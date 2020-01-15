# Filename: mypickle.py
# coding:gbk

import cPickle as pickle

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

summer = Bird()
picklestring = pickle.dumps(summer)
print(picklestring)

fn = 'a.pkl'
with open(fn, 'w') as f:
    picklestring = pickle.dump(summer, f)


fnr = 'a.pkl'
with open(fnr, 'r') as f:
    summer = pickle.load(f)
print(summer.have_feather)
