class A:
    def __init__(self):
        print ("enter A")
        print ("exit A")

class B(A):
    def __init__(self):
        print ("enter B")
        super().__init__()
        print ("exit B")

#toto = B()

class C(B):
    def __init__(self):
        print ("enter C")
        super().__init__()
        print ("exit C")
toto = C()

