class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
    
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance

    def charge(self, price):
        try:
            price = float(price)
            if price + self._balance > self._limit:
                print('Credit card has failed=', self.get_bank())
            else:
                self._balance += price
                return True
        except:
            print('Invalid input')
            return False
        
    def make_payment(self, amount):
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError('Amount must be positive')
            self._balance -= amount
            return True
        except:
            print('Invlid input')
            return False
    
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John', 'Californaia', '5391 0375 9387 5309 2500', 700))
    wallet.append(CreditCard('John', 'Californaia', '3485 0399 3395 1954 3500', 300))
    wallet.append(CreditCard('John', 'Californaia', '5391 0375 9387 5309 5000',1000))

    for val in range(1, 40):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()