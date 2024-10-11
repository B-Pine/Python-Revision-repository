def add_expense(expense_: str, date_, ex_id: int, amount_: float = 0) -> None:
    expenses.append({'details': {'name': expense_, 'date': date_, 'amount':
                    f"${amount_}"}, 'id': ex_id})


expenses = [
    # {'details': {'name': 'McDonald\'s', 'date': '28/09/04', 'amount': 2000},
    #  'id': 0},
    # {'details': {'name': 'Downtown', 'date': '01/04/05', 'amount': 1200},
    #  'id': 1},
]

is_continue = True
expense_id = 0

print("Expense tracker program")
print("*" * 80)

while is_continue:
    print()
    expense_name = input("Where was the expense made? ")
    date = input("date (dd/mm/yy): ")
    amount = float(input("Amount: "))
    input("Click enter to add expense __|")
    add_expense(expense_name, date, expense_id, amount)
    print("Expense added successful.. ")
    print()
    print("\tDisplaying expense entries")

    for expense in expenses:
        for key, value in expense['details'].items():
            print(f"\t\t{key.title()}: {value}")
        print()

    while True:
        is_continue = input('Do you want to add more? (y/n) ')

        if is_continue not in ['y', 'n']:
            print('Enter valid choice!')
            print()
        else:
            is_continue = True if is_continue == 'y' else False
            break

