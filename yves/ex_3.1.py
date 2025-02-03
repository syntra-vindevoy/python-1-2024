def right_justify(txt: str) -> str:
    return ((70 - len(txt)) * " ") + txt


print(right_justify("Monty"))
print(right_justify("Python"))
