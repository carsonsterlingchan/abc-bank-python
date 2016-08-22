"""
Class: DateProvider

Note:

now method is modified to return UTC current date and time.
customedDate method is added to allow user to provide a backdated date if necessary. 


"""
from datetime import datetime


class DateProvider:
    @staticmethod
    def now():
        # Make sure all the dates are in UTC timezone
        return datetime.utcnow()

    @staticmethod
    def customedDate(year, month, day):
        return datetime(year, month, day)
