from models.Expense import Expense

expenses = []

print("Expense Tracker \n")

print("1. Add An Expense \n")

choice = int(input("Type Your Choice: 1 or 2 or 3 or 4 \n"))

try:
    if choice == 1:
        category = input("What does this category falls under ? Food ? Travel ? Recharge ?\n")
        try:
            amount = float(input("How much was the expenditure?\n"))
        except ValueError:
            raise "Start Again and Enter The valid amount"
        description = input("Any Note You Want to add to yourself ?\n")

        temp_id = Expense.shared_variable + 1

        expense = Expense(temp_id, amount, category, description)
        expenses.append(expense)
        print(expense)

    else:
        print("We are adding more features. Regret for inconvenience. Visit Later")

except ValueError:
    raise "Start Again and Enter The Correct Number"
