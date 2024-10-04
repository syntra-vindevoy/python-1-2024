# me = 'Tom'
#
# print(type(me))
#
# print(type(me) == str)
# print(isinstance(me, str))

# class A:
#     pass
#
# class B(A):
#     pass
# b = B()
#
# print(type(b))
# print(type(b) == B)
# print(isinstance(b, B))
# print(type(b) == A)
# print(isinstance(b, A))

x=2
y=3
z=x
x=y
y=z
print (x,y)

x=2
y=3
x=y+x
y=x-y
x=x-y
print (x,y)
x,y=y,x
print (x,y)

n=10000
price=24.95
store_price = price*60/100
shipping = 3*1 + 0.75*(n-1)
total = store_price*n + shipping
print (total)
alt_total = (n*price)*60/100 + shipping #ivm afronding van de 40% korting
print (alt_total)

start= (6*60+52)*60 #sec
slow= 8*60+15
fast = 7*60+12
total_run = 2*slow + 3*fast

stop= total_run + start
uur= (int(stop/3600))
rest_min= stop-uur*3600
min= (int (rest_min/60))
rest_sec= stop-uur*3600-min*60
sec= int(rest_sec)
print (f"{uur}u, {min}m, {sec}s")

#oef 1 functions
def print_t(text):
    print(text)

print_t(3*2)
print_t("tata")

#oef 2 repetition
for i in range(4):
    print(i)

for i in range(1, 4):
    print(i)

for i in range(1, 10, 3):
    print(i)

#oef 3 variable

def add(x,y):
    e=x+y

    print(e)

e=3

print(e)

add(x=2,y=3)

print(e)