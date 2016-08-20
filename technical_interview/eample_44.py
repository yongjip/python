from __future__ import print_function, division

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE altered()")
        super(Child, self).altered()
        print("CHILD, AFTER altered()")


## Line 10: call super with arguments Child and self, then call the function 
## altered on whatever it returns

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override() 

dad.altered()
son.altered()