# Filename:class_human.py

class Human(object):
    laugh = 'hahahahahaha'
    def __init__(self, input_gender):
        self.gender = input_gender
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()
    def printGender(self):
        print self.gender



ching = Human('male')
print ching.gender
ching.printGender()
ching.laugh_100th()

