
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, 2, 3, 4, 5)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="John", age=30)


def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_args_kwargs(1, 2, 3, name="John", age=30)

def  add_numbers(*, a:int,b:int,c:[str]):
    print(a,b,c)

add_numbers(a=2,b=4,c=[1,2,3])

numbers = (1,2,3,4,5,6)

begin,*middel,end = numbers

print(begin,middel,end)

numbers = (1,2,3,4,5,6)
numbers = [*numbers,7,8,9]
print(numbers)

dict = {"a":1,"b":2,"c":3}
numbers = [*dict,7,8,9]
print(numbers)


numbers = (1,2,3,4,5,6)+(7,8,9)
print(numbers)





