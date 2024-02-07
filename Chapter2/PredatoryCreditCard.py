from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    MINIMUN_PAY = 1
    LATE_FEE = 10

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
        self._minimum_pay = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                self._balance += 1
            self._minimum_pay = max(0, self._minimum_pay - price)
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/ 12)
            self._balance *= monthly_factor
        self._num_charges = 0
        if self._minimum_pay > 0:
            self._balance += self.LATE_FEE
        if self._balance > 0:
            self._minimum_pay = self._balance * self.MINIMUN_PAY