n = 100
primes = []

for i in range(2, n + 1):
	for j in range(2, int(i ** 0.5) + 1):
 		if i%j == 0:
 			break
	else:
		primes.append(i)

for k in range(1, 100):
    if k in primes:
        print(k)
    else:
        print(k, end=' ')



