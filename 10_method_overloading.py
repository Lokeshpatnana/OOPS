""" A Function is having default values in the arguments but during 
the function called we pass other values is called as Method-Overloading """

class numbers():
    def sum(self,a=6,c=1,b=3):
        print('Sum=',a+b+c)
N=numbers()
N.sum()
N.sum(54,24,87)
N.sum(55,24)
N.sum(a=42,b=25,c=34)
'''Note: The line numbers 9,10 and 11 are called as method overloading'''