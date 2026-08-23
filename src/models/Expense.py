class Expense:
    shared_variable = 0

    def __init__(self, id, amount, category, description):
        # self.id = shared_variable + 1
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"ID - {self.id} -> Amount - {self.amount} -> Category - {self.category} --> Description - {self.description}"