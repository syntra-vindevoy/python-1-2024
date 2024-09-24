name = "Thomas"

print(type(name))

print(type(name) == str)
print(isinstance(name, str))

class A:
    pass

class B(A):
    pass

a = A()

print(type(a))

b = B()

print(type(b))
print(type(b) == B)
print(isinstance(b, B))

print(type(b) == A)         #type doesn't take into account inheritance
print(isinstance(b, A))     #isinstance takes into account inheritance --> usage of isinstance is better!!!!

print(type((4,2)))

#Excersie 1.9.5
time = (42 * 60) + 42
print(time)

mile = (10 / 1.61)
print(mile)

sec_per_mile = time / mile
print(sec_per_mile)

min_per_mile = sec_per_mile // 60
rem_sec_mile = sec_per_mile % 60
print(min_per_mile)
print(rem_sec_mile)

miles_h = (mile / time) * 3600
print(miles_h)
