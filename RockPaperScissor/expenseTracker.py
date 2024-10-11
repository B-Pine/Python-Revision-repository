import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import DateEntry


def add_expense() -> None:
    """Add expense on history tab"""
    global ex_id
    # Capturing entries from the user
    expense_ = expense_name_receiver.get()
    date_ = date_receiver.get_date()
    amount_ = float(float_checker(amount_receiver.get()))
    # checking if the entry box are empty to add expense
    if expense_ == '' or date_ == '' or amount_ < 0:
        messagebox.showwarning('Warning', 'All fields must be filled')
    else:
        expenses.append({'details': {'name': expense_.title(), 'date': date_,
                                     'amount':
                                         f"${amount_:.2f}", 'delete': 'x'},
                         'id': ex_id})

        # Clearing fields for new entry
        expense_name_receiver.delete(0, tkinter.END)
        date_receiver.set_date('01/01/2019')
        amount_receiver.delete(0, tkinter.END)
        # amount_receiver.insert(0, '0')
        ex_id += 1
        messagebox.showinfo('Success', 'Expense added successful')
        draw_entries(expenses)


def float_checker(amount: str):
    if amount.isnumeric():
        return amount
    else:
        # messagebox.showwarning('Warning', 'Invalid amount value!')
        amount_receiver.delete(0, tkinter.END)
        return -1


def headings_drawer() -> None:
    """Draw headings of expense entries table (history tab)"""
    headings = ['Exp location', 'Date', 'Amount', '']
    column = 0
    for head in headings:
        (tkinter.Label(expense_frame, text=head, background='grey')
         .grid(row=0,
               column=column,
               sticky='ew',
               padx=10,
               ipadx=30))
        column += 1


def draw_entries(expenses_list: list) -> None:
    """Draw new inserted expense entries to the table"""
    global entry_row
    global entry_column

    expense_object = expenses_list[-1]
    for value in expense_object['details'].values():
        Label(expense_frame, text=value, padding=5).grid(
            row=entry_row, column=entry_column, sticky='ew', padx=10)
        entry_column += 1
    entry_row += 1
    entry_column = 0


# main configuration
master = tkinter.Tk()
master.title('Expense tracker')
master.geometry('520x480')
master.configure(padx=5)

# Widgets for main headings
Label(master, text='Expense Tracker', font=('Arial', 20)).grid(row=0,
                                                               column=0,
                                                               columnspan=4)
Label(master, text='Add New Item:', font=('arial', 15),
      foreground='green').grid(row=1, column=0, columnspan=4)

# Widgets to receive expense details
# Receiver Frame
receiver_frame = Frame(master, padding=15)
receiver_frame.grid(row=3, column=0, rowspan=2, columnspan=4, sticky='ew')

# expense name
Label(receiver_frame, text='Item name: ').grid(row=0, column=0, sticky='w')
expense_name_receiver = Entry(receiver_frame)
expense_name_receiver.grid(row=0, column=1, sticky='ew', ipady=5)
# date
Label(receiver_frame, text='Date: ', padding=10).grid(row=0,
                                                      column=2,
                                                      sticky='w')
date_receiver = DateEntry(receiver_frame, selectmode='day', year=2024,
                          month=1, day=1)
date_receiver.grid(row=0, column=3, sticky='ew', ipady=5)
# amount
Label(receiver_frame, text='Amount: ').grid(row=1, column=0, sticky='w')
amount_receiver = Entry(receiver_frame)
# amount_receiver.insert(0, '0')
amount_receiver.grid(row=1, column=1, sticky='ew', ipady=5)
# Add expense button
tkinter.Button(receiver_frame, text='Add Expense', bg='Green',
               fg='white', activebackground='mediumseagreen',
               command=add_expense).grid(row=1, column=3, sticky='ew')

# Defining frame for entries
expense_frame = tkinter.Frame(master)
expense_frame.grid(row=5, column=0, columnspan=4, sticky='ew')
# Table headings
headings_drawer()

# They're globals which is used to update the entries rows and column
entry_row = 1
entry_column = 0

expenses = []

# expense id
# will be used to delete certain item in future
ex_id = 0

master.mainloop()
print(expenses)
