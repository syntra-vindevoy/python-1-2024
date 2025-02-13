

class Variable:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        var_type = int

        self.var_type = var_type

class VariableStore:
    def __init__(self):
        self.variables = {}

    def add(self, var: Variable):
        self.variables[var.key] = var

    def get(self, key) -> Variable:
        return self.variables[key]

store = VariableStore()

vars = ["toto=tata", "tutu=titi"]

for v in vars:
    key, value = v.split("=")

    var = Variable(key=key, value=value)
    store.add(var)


print(store.get("tutu").var_type)
print(store.get("toto").value)



