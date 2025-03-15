class A:
    def actie(self):
        print("A actie")


class B(A):
    def actie(self):
        super().actie()
        print("B actie")


class C(A):
    def actie(self):
        super().actie()
        print("C actie")


class D(B, C):
    def actie(self):
        super().actie()
        print("D actie")


d = D()
d.actie()
print(D.__mro__)
print(D.mro())
