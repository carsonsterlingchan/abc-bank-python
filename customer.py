"""
Class: Customer

Note:

Added transferAccounts method to allow user to transfer money between his/her accounts in the bank.

In statementForAccount method, totalSummary is changed to use account.sumTransactions() method.

"""

from abcbank.account import CHECKING, SAVINGS, MAXI_SAVINGS

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def openAccount(self, account):

        self.accounts.append(account)
        return self

    def transferAccounts(self, fromAcct, toAcct, amount):

        # Make sure there is sufficent amount of money in the fromAcct before transfer
        fromAcctBal = fromAcct.sumTransactions()
        if fromAcctBal == 0 or fromAcctBal < amount:
            raise Exception('The source account does not have sufficient funds for transfer.')

        fromAcct.withdraw(amount)
        toAcct.deposit(amount)
        
    def numAccs(self):
        return len(self.accounts)

    def totalInterestEarned(self):        
        return sum([a.interestEarned() for a in self.accounts])

    # This method gets a statement
    def getStatement(self):
        # JIRA-123 Change by Joe Bloggs 29/7/1988 start
        statement = None  # reset statement to null here
        # JIRA-123 Change by Joe Bloggs 29/7/1988 end
        totalAcrossAllAccounts = sum([a.sumTransactions() for a in self.accounts])
        statement = "Statement for %s" % self.name
        for account in self.accounts:
            statement = statement + self.statementForAccount(account)
        statement = statement + "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts)
        return statement

    def statementForAccount(self, account):
        accountType = "\n\n\n"
        if account.accountType == CHECKING:
            accountType = "\n\nChecking Account\n"
        if account.accountType == SAVINGS:
            accountType = "\n\nSavings Account\n"
        if account.accountType == MAXI_SAVINGS:
            accountType = "\n\nMaxi Savings Account\n"
        transactionSummary = [self.withdrawalOrDepositText(t) + " " + _toDollars(abs(t.amount))
                              for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(account.sumTransactions())
        return accountType + transactionSummary + totalSummary

    def withdrawalOrDepositText(self, transaction):
        if transaction.amount < 0:
            return "withdrawal"
        elif transaction.amount > 0:
            return "deposit"
        else:
            return "N/A"


def _toDollars(number):
    return "${:1.2f}".format(number)
