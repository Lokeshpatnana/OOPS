""" All Classes having different names but having same function names and 
 inheriting the properities of parent class(single)  is called as Polymorphism."""

class Animal:
    def noise(self):
        pass
class cat(Animal):
    def noise(self):
        print("Meoow")
class dog(Animal):
    def noise(self):
        print("Woof")
class monkey(Animal):
    def noise(self):
        print("Urrrr")
a=cat()
a.noise()
b=dog()
b.noise()
c=monkey()
c.noise()