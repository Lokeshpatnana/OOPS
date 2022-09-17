""" Part-2 Calling with the help of an object """
"""Parent Class"""
class Animal:
    livingthing=True
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping")

"""Child Class"""
class goat(Animal):
    def grass(self):
        print("Its eating grass")
    def herb(self):
        print("It is herbivorus")
    def sleep(self):
        print("Don't sleep you are 710Rs kg")
a=Animal()
print(a.livingthing)
a.eat()
a.sleep()

b=goat()
b.grass()
b.herb()
b.sleep()
print(b.livingthing)
b.eat()
a.grass()  # Attribute error