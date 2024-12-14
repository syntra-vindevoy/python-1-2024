count = 1
i = 1
while count < 10000:
    i += 2
    for k in range(2, 1+int((i+1)**0.5)):
        if i%k == 0:
            break
    else:
        count += 1

print(i)