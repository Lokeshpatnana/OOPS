""" Both Parent and child having the same function names but the child class
 over rides the parent class when function called is cllaed as Method-Overriding """

class parent():
    def study(self):
        print("Keep Studying")
class child(parent):
    def study(self):
        print("Take a break")
a=parent()
a.study()
child().study()



class Parent:   #Parent class is Main Class
    def name(self):
        print("It is a Parent Class")
class Child(Parent):  # Child class is Sub class
    def name(self):
        print("It is a Child Class")
b=Parent()
b.name()