""" A Single child can inheriting the properities of two parent classes are called as Multiple Inheritance """

class father():
    food="Yes"
    Shopping="Yes"
    Work="No"
    def bank(self):
        print("Savings Account")
class mother():
    education="Yes"
    Movie="No"
    food="No"
    def privacy(self):
        print("No Privacy")
# class Lokesh(mother,father):
class Lokesh(father,mother):
    def clothes(self):
        print("clothes for me")
    def phone(self):
        print("Phone for me")
print("Lokesh ate food "+Lokesh.food)
print("Lokesh go to shopping "+Lokesh.Shopping)
print("the work for lokesh today is "+Lokesh.Work)
a=Lokesh()
a.bank()
a.clothes()
a.phone()
print(a.Shopping)
print("Education of lokesh "+a.education)
print("watching movie for the lokesh "+a.Movie)
a.privacy()