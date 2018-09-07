import re
from applications.FristSample.common.common_var import Regrex as regex

class BaseInterface:

    def isNotEmpty(self,params):
        return bool(params and params.strip())

    def isDate(self, date):
        check = re.compile(regex.regrex_day)
        return check.match(date)

    def isAlnumric(self, age):
        return age.isnumeric()

    def isEmail(self, email):
        check = re.compile(regex.regrex_email)
        return check.match(email)
