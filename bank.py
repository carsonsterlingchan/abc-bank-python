"""
Class: Bank

Note:

getFirstCustomer method is fixed.  It only prints out the firstCustomer name if there is a customer.

"""

from abcbank.customer import Customer

class Bank:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        self.customers.append(customer)
    def customerSummary(self):
        summary = "Customer Summary"
        for customer in self.customers:
            summary = summary + "\n - " + customer.name + " (" + self._format(customer.numAccs(), "account") + ")"
        return summary
    def _format(self, number, word):
        return str(number) + " " + (word if (number == 1) else word + "s")
    def totalInterestPaid(self):
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total
    def getFirstCustomer(self):
        if len(self.customers) == 0:
            raise Exception("Bank has no customers.")
        return self.customers[0].name

