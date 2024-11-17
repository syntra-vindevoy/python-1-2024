nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num,letter)
    if num == 3:
        print('found')
        break #or continue to keep going
    print(num)

for i in range(1,11): #or for i in range(10)
    print(i)

x = 1

while x<10:
    if x == 5:
        break
    print(x)
    x += 1

