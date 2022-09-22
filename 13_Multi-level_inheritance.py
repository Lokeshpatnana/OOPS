""" A child class can inheriting the properities of parent and grand parent class and a parent 
can inheriting the properities of only grand parent class are called Multi-level Inheritance """

class gfather():
    bike="Yes"
    pocketmeoney="Yes"
    enjoylife="Yes"
    def bank(self):
        print("Savings Account")
class father(gfather):
    def clothes(self):
        print("First for my dad")
    def phone(self):
        print("My son is studying so it can be useful to him to earn more skills")
class me(father):
    def job(self):
        print("First get and happiness from my father")
    def work(self):
        print("Always work hard to proud my parents well in society")
print("i want to buy a bike for my child "+father.bike)
print("I want to give pocket money for his usages "+father.pocketmeoney)
print("Now i am doing hardwork but my son don't do it he enjoy life "+father.enjoylife)
a=father()
a.bank()
a.clothes()
a.phone()

print("For my grand child to ride a bike "+me.bike)
print("I want to give him a pocket money to enjoy "+me.pocketmeoney)
print("Me and my son doing hard work but my grand son don't do any work "+me.enjoylife)
b=me()
b.bank()
b.phone()
b.clothes()
b.job()
b.work()