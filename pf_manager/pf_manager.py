import pandas as pd

# sample data: Date, Description, Amount
data = {
  'Date': ['2023-10-01', '2023-10-02', '2023-10-03'],
  'Description': ['Bought groceries', 'Paid rent', 'Dined out'],
  'Amount': [-50, -1000, -30]
}
expenses_df = pd.DataFrame(data)
print(expenses_df)

print("-" * 20)


"""Adding a new expense"""
new_expense = {'Date': '2023-10-04', 'Description': 'Bought a book', 'Amount': -20}
expenses_df = expenses_df.append(new_expense, ignore_index=True)
print(expenses_df)

print("-" * 20)


# Querying for a specific expense based on its description
"""Find expenses greater than 40"""

high_expenses = expenses_df['Amount'] > -40 # returns a boolean mask
print(high_expenses)


# Basic Operations
total_expenses = expenses_df['Amount'].sum()
print(f"Total expenses: {total_expenses}")

print("-" * 20)
expenses_df['date'] = pd.to_datetime(expenses_df['Date'])
expenses_df = expenses_df.sort_values(by='Date')
print(expenses_df)

#save the df to a csv file
expenses_df.to_csv('expenses.csv', index=False)
loaded_df = pd.read_csv('expenses.csv')
print(loaded_df)

print("-" * 20)

