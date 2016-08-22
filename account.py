"""
Class:  Account

Note: 
 
__init__ is changed to accept one more parameter, openDate.  
openDate is the date the account is opened.  It is used for interest calculation.
If it is not passed during instantiation, openDate will be defaulted to current UTC datetime.

deposit and withdraw methods are also modified to accept one more parameter, transDate.
transDate is used for calculating interest rate.  It is particuarly useful for maxi_saving_accounts interest calculation.
If transDate is not set, it will be defaulted to current UTC datetime.

There are two interest calculations: simple daily accrued interest (_cal_Simple_AccruedInt)
and compound daily interest (_cal_Compound_AccruedInt).
Since I am not sure which solution you prefer, it is currently set to use simple daily accrued interest calcuation.

sumTransactions method is modified to calculate the amount of withdrawls for the past 10 days when checkAllTransactions
is set to False.  It is particuarly useful for maxi_saving_accounts interest calculation.
 
"""

from abcbank.transaction import Transaction
from abcbank.date_provider import DateProvider

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2

class Account:
    def __init__(self, accountType, openDate=None):
        self.accountType = accountType
        self.transactions = []
        if openDate is None:
            self.openDate = DateProvider().now()
        else:
            self.openDate = openDate

    def deposit(self, amount, transDate=None):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount,transDate))


    def withdraw(self, amount, transDate=None):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            # Find out if the account has enough money for withdrawl.
            if self.sumTransactions() < amount:
                raise Exception("Withdrawal amount exceeds the balance of the account.")
            else:
                self.transactions.append(Transaction(-amount,transDate))
                    

    def _cal_Simple_AccruedInt(self, amount, rate):
        days_accumlated = (DateProvider().now() - self.openDate).days
        return amount * (rate / 365) * days_accumlated

    def _cal_Compound_AccruedInt(self, amount, rate):
        days_accumlated = (DateProvider().now() - self.openDate).days
        #return amount * (1 + rate/365) ** 365
        return amount * (1 + rate/365) ** days_accumlated
    
    def interestEarned(self):
        amount = self.sumTransactions()

        interestFunc = self._cal_Simple_AccruedInt
        #interestFunc = self._cal_Compound_AccruedInt
        
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return interestFunc(amount,0.001)
            else:
                return interestFunc(1000,0.001) +  interestFunc((amount-1000),0.002)
            
        if self.accountType == MAXI_SAVINGS:
            ten_days_withdrawl_amt = self.sumTransactions(checkAllTransactions=False)
            if ten_days_withdrawl_amt > 0:
                return interestFunc(amount, 0.001)
            else:
                return interestFunc(amount, 0.05)
        else:
            return interestFunc(amount,0.001)

    def sumTransactions(self, checkAllTransactions=True):
        if checkAllTransactions:
            return sum([t.amount for t in self.transactions])
        else:
            # Only calculate the sum of withdrawls for the past 10 days
            now = DateProvider().now()
            return -1 * sum([t.amount for t in self.transactions if (0 <= (now - t.transactionDate).days  <=10) and t.amount < 0])
