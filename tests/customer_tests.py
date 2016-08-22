from nose.tools import assert_equals, assert_raises, nottest

from abcbank.account import Account, CHECKING, SAVINGS, MAXI_SAVINGS
from abcbank.customer import Customer


def test_statement():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    assert_equals(oscar.numAccs(), 1)


def test_twoAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 2)


def test_threeAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    oscar.openAccount(Account(MAXI_SAVINGS))
    assert_equals(oscar.numAccs(), 3)

def test_withdrawl_error():
    checkingAccount = Account(CHECKING)
    david = Customer("David").openAccount(checkingAccount)
    checkingAccount.deposit(100.0)
    assert_raises(Exception, checkingAccount.withdraw, 200)

def test_transfer():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    henry.transferAccounts(savingsAccount, checkingAccount, 1000)
    assert_equals(savingsAccount.sumTransactions(), 3000)
    assert_equals(checkingAccount.sumTransactions(), 1100)
    
def test_transfer_with_insufficientfund():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    john = Customer("John").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    assert_raises(Exception, john.transferAccounts, (savingsAccount, checkingAccount, 5000))

