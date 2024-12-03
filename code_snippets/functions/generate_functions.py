def create_method(n):
    def method():
        print(f"method_{n}")

    return method


# Generate functions and store them in a dictionary
methods = {i: create_method(i) for i in range(1, 8)}

# Now you can call the generated functions
methods[1]()
methods[2]()
methods[3]()
methods[4]()
methods[5]()
methods[6]()
methods[7]()
