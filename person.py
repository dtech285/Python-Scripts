#!/usr/bin/env python3

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
        

if __name__ == '__main__':
    """self test code - this only runs if file is called directly.
    # does not run if imported. """
    
    bob = Person('Bob Smith')                           # Tests the class
    sue = Person('Sue Jones', job='dev', pay=100000)    # Runs _init_ automatically
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print('%.2f' % sue.pay)
    print(sue)
    

    
