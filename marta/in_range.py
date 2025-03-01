total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(7):
    expenses.append(float(input("Enter an expense:")))
total = sum(expenses)

print("You spent $", total, sep='')
