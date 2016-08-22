"""
Note:

There are two sets of interest calculation tests:  Simple Daily Interest and Compound Daily Interest.
The Compound Daily Interest set is turned off.  Please turn it on if that is the calculation you are looking for.
Make sure interestFunc is set to self._cal_Compound_AccruedInt in interestEarned method in Account class file.

"""

from nose.tools import assert_equals, assert_raises, nottest

from abcbank.account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from abcbank.bank import Bank
from abcbank.customer import Customer

from datetime import datetime, time
from dateutil.relativedelta import relativedelta

# Figure out the date one year from now.
# This is easier for calculate the interest
backDated_one_year = datetime.utcnow().date() + relativedelta(days=-365)
backDated_one_year = datetime.combine(backDated_one_year, time.min)

def test_customer_summary():
    bank = Bank()
    john = Customer("John").openAccount(Account(CHECKING))
    bank.addCustomer(john)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (1 account)")

def test_firstCustomer():
    bank = Bank()
    assert_raises(Exception, bank.getFirstCustomer)
    

def test_checking_account():
    # Simple Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(CHECKING,backDated_one_year)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0)
    assert_equals(bank.totalInterestPaid(),  0.10000000000000002)


def test_savings_account():
    # Simple Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(1500.0)
    assert_equals(bank.totalInterestPaid(), 2.00)


def test_maxi_savings_account():
    # Simple Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(3000.0)
    assert_equals(bank.totalInterestPaid(), 150.0)
    

def test_maxi_savings_acct_diffInt():
    # Simple Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(3000.0)
    checkingAccount.withdraw(1000.0)
    assert_equals(bank.totalInterestPaid(), 2.0)

@nottest
def test_checking_account_2():
    # Compond Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(CHECKING,backDated_one_year)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0)
    assert_equals(bank.totalInterestPaid(),  100.10004987954706 )

@nottest
def test_savings_account_2():
    # Compond Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(1500.0)
    assert_equals(bank.totalInterestPaid(), 1502.0014967172629)

@nottest
def test_maxi_savings_account_2():
    # Compond Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(3000.0)
    assert_equals(bank.totalInterestPaid(), 3153.802489402342)

@nottest
def test_maxi_savings_acct_diffInt_2():
    # Compond Daily Interest Calculation Test.
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS,backDated_one_year)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(3000.0)
    checkingAccount.withdraw(1000.0)
    assert_equals(bank.totalInterestPaid(), 2002.000997590941)

