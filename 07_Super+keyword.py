class A:
    def loki(self):
        print("I'm a Parent Class")
class B(A):
    def loki(self):
        super().loki()
        print("I'm a Child Class")
        super().loki()
C=B()
C.loki()