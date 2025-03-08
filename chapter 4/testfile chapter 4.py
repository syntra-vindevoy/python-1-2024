def dom(y, m):
    return 31

#assert dom(2024,1) == 31
#assert dom(2024, 2) == 32

def divide (a, b):
    return a / b

print (divide(4,2))
print (divide(b=9, a=2))

def no_used (a,b=10,c=100): #standaard waarde indien niets gegeven
    print (a,b,c)
no_used(1,2,3)
no_used(a=5, b=8)
no_used(1,2)

def named_para (*, een, twee):
    print (een, twee)
#named_para(5,10) #werkt niet door sterretje. Verplicht parameters te benoemen
named_para(een=52, twee=89)

def type_hint (tekst: str, nummer: int, r:int= 50 ):
    print (tekst)
    print (nummer, r)
type_hint(tekst= 55, nummer= 8) #enkel warning ivm string, wordt niet afgedwongen
type_hint(tekst="hey", nummer=80, r=1)

z:int = 5
f:str = "string"

lst = [1,5,3,4]
#lst = lst.sort()
#print(lst) #werkt niet omdat sort niets teruggeef
lst.sort()
for i in lst:
    print(i)
print (lst)
