""" Operator Overloading means giving extended meaning beyond their predefined operational meaning.
 For example operator '+' is used to add two integers as well as join two strings and merge two lists. 
 It is achievable because '+' operator is overloaded by int class and str class. You might have noticed
  that the same built-in operator or function shows different behavior for objects of different classes,
   this is called Operator Overloading """

a=15 ; b=65
print(a+b)

c="Hello" ; d="Lokesh"
print(c+d)

e=[5,8,7] ; f=[1,6,9]
print(e+f)
print(e[:]+f[:])