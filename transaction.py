"""
Class:  Transaction

Note:

The class init method is modified to take an additional parameter: transDate.
transDate is for interest calculation purpose.  If transDate is not passed,
it will be defaulted to current UTC datetime.

"""


from abcbank.date_provider import DateProvider

class Transaction:
    def __init__(self, amount, transDate=None):
        self.amount = amount
        if transDate is None:
            self.transactionDate = DateProvider.now()
        else:
            self.transactionDate = transDate
