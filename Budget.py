
class Budget:

    _balance = 0

    def __init__(self, name):
        self.name = name

    def deposit(self, amount):
        try:
            self._balance += int(amount)
            print(f'You have transferred, {amount} to your {self.name}-account successfully')
        except: 
            print('You cannot deposit that amount, please try again')

    def withdraw(self, amount):
        try:
            if self._balance - int(amount) < 0:
                print('You do not have enough money for this withdrawal. Please try again.')
            else:
                self._balance -= int(amount)
                print(f'You have withdrawn, {amount} from your {self.name}-account successfully.')               
        except: 
            print('You cannot withdraw that amount, please try again.')

    def check_balance(self):
        return f'Your {self.name}-account balance is {self._balance}'

    def transfer(self, amount, object):
        try:
            if self._balance - int(amount) < 0:
                print('You do not have enough money for this transfer. Please try again.')
            elif not isinstance(object, Budget):
                print('Sorry, you can only make transfers to other budget accounts.')
            else:
                self._balance -= int(amount)
                object.deposit(amount)    
        except: 
            print('You cannot transfer that amount, please try again.')
 
    def __repr__(self):
        return f'This is a budget class for - {self.name}, \nYou can use the following methods: deposit, withdraw, check_balance and transfer'
