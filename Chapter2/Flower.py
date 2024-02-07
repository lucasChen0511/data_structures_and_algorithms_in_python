class Flower:
    def __init__(self, name=None, amount=0, price=10):
        self._name = name
        self._amount = amount
        self._price = price
    
    def set_name(self, name):
        try:
            self._name = str(name)
        except:
            print('Invalid input for a name, it must be a string')
    
    def set_amount(self, amount):
        try:
            self._amount = amount
        except:
            print('Invalid input')
    
    def set_price(self, price):
        try:
            self._price = float(price)
        except:
            print('Invalid input')

    def get_name(self):
        return self._name
    def get_amount(self):
        return self._amount
    def get_price(self):
        return self._price

if __name__ == '__main__':
    Dand =Flower('Dandelion', 5, 90)
    print(Dand.get_name(), Dand.get_amount(), Dand.get_price())

    Rose = Flower()
    Rose.set_name('Blue Rose')
    Rose.set_amount(9)
    Rose.set_price(200)
    print(Rose.get_name(), Rose.get_amount(), Rose.get_price())
