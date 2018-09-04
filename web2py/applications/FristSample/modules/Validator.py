import re
from Common import Regrex as regex
class Validate(object):
    def __init__(self):
        return
    def isDate(self,date):
        check = re.compile(regex.regrex_day)
        return check.match(date)

    def isAlnumric(self,age):
        return age.isnumeric()

    def isEmail(self,email):
        check = re.compile(regex.regrex_email)
        return check.match(email)




