#Chapter 01: Exercises
import math

print(25.8 / 2)
print(25.8 // 2)        #Integer div is always flooring down
print("#" * 50)

print(round(21.4))      #When < .5 --> rounding down
print(round(21.6))      #When > .5 --> rounding up

                        #When == .5
print(round(21.5))      #Both give 22 --> round of .5 will go to the nearest even number
print(round(22.5))
print(int(21.9))        #Making an Int of a Real doesn't do any round operation on them, it just drops the numbers after the comma
print(int(22.5))
print("#" * 50)

pi = math.pi
print(pi)

round_pi = round(pi)
print(round_pi)
round_pi = round(pi, 3)
print(round_pi)
print("#" * 50)

print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))
print("#" * 50)



#Excersie 1.9.5
sec = (42 * 60) + 42
print(sec)

miles = (10 / 1.61)
print(miles)

sec_mile = sec / miles
print(sec_mile)

min_mile = sec_mile // 60
rem_sec_mile = sec_mile % 60
print(min_mile)
print(rem_sec_mile)

miles_h = (miles / sec) * 3600
print(miles_h)