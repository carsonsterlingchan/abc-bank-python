from nose.tools import assert_is_instance, assert_equal

from abcbank.transaction import Transaction
from abcbank.date_provider import DateProvider
from datetime import datetime

def test_type():
    t = Transaction(5)
    assert_is_instance(t, Transaction, "correct type")

def test_transDate():
    t = Transaction(10, DateProvider().customedDate(2016, 8, 20))
    assert_equal(t.transactionDate, datetime(2016, 8, 20))
