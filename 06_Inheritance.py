"""Part-1"""
"""Parent Class"""
class animal:
    livingthing=True
    def eat():
        print('Eating')
    def sleep():
        print('Sleeping')
"""Child Class"""
class horse(animal):
    def grass():
        print('Eating Grass')
    def herb():
        print('It ia a Herbivorus')
    def sleep():
        print("You cannot sleep it's time for ride")
print(cow.livingthing) # Here Child class and accessing the parent class variable
print(animal.livingthing) # Here the parent class and accessing class variable
cow.grass()
cow.herb()
cow.eat()  # here the function is not availabe the child class is taking the function from parent class
cow.sleep()  # if the parent and child class having the same functions here first priority will given to child class
animal.eat()
animal.sleep()
animal.herb() # here parent class is not have herb function but it cannot taken the function from child class
