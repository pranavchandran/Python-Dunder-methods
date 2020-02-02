from functools import total_ordering

class Account:
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):

        return 'Account {}, {} '.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(            
            self.owner, self.amount)


# print(acc.owner,acc.amount)
# print(repr(acc))
# print(str(acc))
# print(acc)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Please use int for amount')
        self._transactions.append(amount)

    
#  In Python, the main purpose of Property() function is to create property of a class. Return: Returns a property attribute from the given getter, setter and deleter.
    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)
    
    def __getitem__(self,position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self,other):
        return self.balance == other.balance
    
    def __lt__(self,other):
        return self.balance < other.balance

    def __add__(self,other):
        owner = '{}&{}'.format(self.owner,other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner,start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    def __call__(self):
        print('start amount: {}'.format(self.amount))
        print('Transactions')

        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))

    def __enter__(self):
        print('Enter With: Making backup of transactions for rollback')
    # _ returns the value of last executed expression value in Python Prompt/Interpreter
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self,exc_type,exc_value,exc_tb):
        print('Exit With :',end='')
        if exc_type:
            self._transactions = self._copy_transactions
            print('Rolling back to previous transactions.')
            # print(f'Transaction resulted in {exc_type}({exc_value})')

        else:
            print('Transaction OK')

def validate_transaction(acc,amount_to_add):
    with acc as a:
        print(f'Adding {amount_to_add} to account')
        a.add_transaction(amount_to_add)
        print(f'New balance wouled be: {a.balance}')
        if a.balance < 0:
            raise ValueError('Sorry cannot go in Debt!')

        # Methods for validating the accounts

# acc3 = Account('kuttu',5000)
# print(f'\nBalance start: {acc3.balance}')

# validate_transaction(acc3,1000)

# print(f'\nBalance End: { acc3.balance}')

        # Another method for dont falling to debt in Bank

acc3 = Account('kuttu',5000)
print(f'\nBalance start : {acc3.balance}')

try:
    validate_transaction(acc3,-5050)
except ValueError as exc:
    print(exc)
print(f'\nBalance end: {acc3.balance}')

    









        
acc = Account('Bob',10)
acc.add_transaction(100)
acc.add_transaction(-20)
acc.add_transaction(5000)
acc.add_transaction(150)





# print('**********Account Statement**********')

# for x,y in enumerate(acc):
    # print(x,y)

# print(f'{acc.owner} : ',acc.balance ,'Total transactions :',(len(acc)))
# If you want to see the Latest transaction to old Tracsaction.
# print('From Latest Transactions to old',list(reversed(acc)))

# it works by dunder method __eq__ and __lt__

# print(acc2>acc)
# print(acc2<acc)
# print(acc == acc2)

# ***************************************

# it works by __add__ function refer its important

# acc2 = Account('Tim',5000)
# acc2.add_transaction(2500)
# acc3 = acc2 + acc

# print(acc3._transactions)

# It works by __call__  function.

# print(acc2())

# *************************************************

# Context Manager Support and the With Statement: __enter__, __exit__
# And Validation Last dunder techniques *********




