class A:
    def __init__(self):

        self.a = 1

        print("enter A")
        super().__init__()
        print("exit A")

class B:
    def __init__(self):

        self.b = 2

        print("enter B")
        super().__init__()
        print("exit B")


class C(B, A):
    def __init__(self):
        print("enter C")
        super().__init__()
        #A.__init__(self)
        #B.__init__(self)
        print("exit C")

toto = C()

# print(toto.a)
# print(toto.b)

print(C.mro())

b = B()
print(B.mro())