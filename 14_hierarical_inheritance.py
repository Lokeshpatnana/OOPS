""" A Child class is inheriting the properities of parent class and grand parent class ,and parent
 class can inheriting the properities of only grand parent class are called Hierarical Inheritance """

class parent():
    movie="Yes"
    work="Yes"
    shopping="No"
    def bank(self):
        print("Current Account")
class fchild(parent):
    def clothes(self):
        print("Clothes of first child")
    def phone(self):
        print("Phone of first child")
class schild(parent):
    def laptop(self):
        print("laptop of second child")
    def car(self):
        print("car of second child")
print("Going to movie with girlfriend "+fchild().movie)
print("getting a job in reputed company "+fchild().work)
print("Is there any to go shopping "+fchild().shopping)
a=fchild()
a.bank()
a.clothes()
a.phone()
# a.laptop()  # attributeerror

b=schild()
b.bank()
b.shopping
b.laptop()
b.car()