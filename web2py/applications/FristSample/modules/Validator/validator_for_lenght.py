
from base_module import BaseInterface
class Validate(BaseInterface):
    def __init__(self):
        BaseInterface.__init__(self)

    def is_max_lenght_of_order(self,order):
        return len(order)

    def is_max_lenght_of_user(self,user):
        return len(user)

    def is_max_lenght_of_str(self,str):
        return len(str)

    def is_right_age(self,age):
        if (int(age) > 1 and int(age) <100):
            return True
        else :
            return False

    def list_vars(self,order_id, user_id, ngaymua, name, eventname, age, phone, email, cachthanhtoan, phuongthucnhan,
                  quanhuyen):
        return {'order_id': order_id, 'user_id': user_id, 'ngaymua': ngaymua, 'name': name, 'eventname': eventname,
                'age': age, 'phone': phone, 'email': email, 'cachthanhtoan': cachthanhtoan,
                'phuongthucnhan': phuongthucnhan, 'quanhuyen': quanhuyen,
                'message_order': '', 'message_user': '', 'message_ngaymua': '', 'message_name': '',
                'message_eventname': '', 'message_age': '',
                'message_phone': '', 'message_email': '', 'message_cachthanhtoan': '', 'message_phuongthucnhan': '',
                'message_quanhuyen': ''}
