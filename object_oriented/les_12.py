# class A:
#     def __init__(self):
#         print ("enter A")
#         print ("exit A")
#         self.a = 5
#
# class B:
#     def __init__(self):
#         print ("enter B")
#         print ("exit B")
#         self.b = 8
#
# #toto = B()
#
# class C(A, B):
#     def __init__(self):
#         print ("enter C")
#         super().__init__()  #super is hier enkel de eerste in de lijst, voert B niet uit
#         print ("exit C")
# toto = C()
#
# print (toto.a)
# print (toto.b)

class A:
    def __init__(self):
        print ("enter A")
        super().__init__()
        print ("exit A")
        self.a = 5

class B:
    def __init__(self):
        print ("enter B")
        super().__init__()
        print ("exit B")
        self.b = 8

class C(B, A):
    def __init__(self):
        print ("enter C")
        super().__init__()
        # A.__init__(self)
        # B.__init__(self)
        print ("exit C")
toto = C()

print (toto.a)
print (toto.b)