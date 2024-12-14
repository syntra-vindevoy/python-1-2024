def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def check_numbers():
    a = int(input("What is the number you want the Fibonacci sequence of?"))

    if a <= 0:
        print("Positive integer please")
    else:
        print("Fibonacci sequence:")
        for i in range(a):
            print(recur_fibo(i))


check_numbers()