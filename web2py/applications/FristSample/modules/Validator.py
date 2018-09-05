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

    def isNotEmpty(self,params):
        return bool(params and params.strip())

    def list_vars(self,order_id, user_id, ngaymua, name, eventname, age, phone, email, cachthanhtoan, phuongthucnhan,
                  quanhuyen):
        return {'order_id': order_id, 'user_id': user_id, 'ngaymua': ngaymua, 'name': name, 'eventname': eventname,
                'age': age, 'phone': phone, 'email': email, 'cachthanhtoan': cachthanhtoan,
                'phuongthucnhan': phuongthucnhan, 'quanhuyen': quanhuyen,
                'message_order': '', 'message_user': '', 'message_ngaymua': '', 'message_name': '',
                'message_eventname': '', 'message_age': '',
                'message_phone': '', 'message_email': '', 'message_cachthanhtoan': '', 'message_phuongthucnhan': '',
                'message_quanhuyen': ''}
