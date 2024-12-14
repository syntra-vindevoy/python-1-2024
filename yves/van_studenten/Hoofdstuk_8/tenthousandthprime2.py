import time

st = time.time()

i = 2
count = 1

while True:
    i += 1
    prime = True
    div = 2
    limit = (i**0.5) + 1
    while div < limit:
        if not (i % div):
            prime = False
            break
        else:
            div += 1
    if prime:
        count += 1
    if count == 100000:
        print("The 100000th prime number is %s" %i)
        break

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')