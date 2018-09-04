from gluon.dal import DAL ,Field

class Connect(object):
    def __init__(self):
        self.db = DAL("mysql://root:root@localhost/web2py")
        self.define_table()

    def define_table(self):
        # Create table
        self.db.define_table('orders',
                             Field('order_id', 'string', required=True),
                             Field('user_id', 'string'),
                             Field('ngay_mua', 'string'),
                             Field('name', 'string'),
                             Field('event_name', 'string'),
                             Field('age', 'integer'),
                             Field('phone', 'string'),
                             Field('email', 'string'),
                             Field('cach_thanh_toan', 'string'),
                             Field('phuong_thuc_nhan', 'string'),
                             Field('quan_huyen', 'string'),
                             primarykey=['order_id'])

        # Create table
        self.db.define_table('order_detail',
                             Field('event_id', 'string', required=True),
                             Field('user_id', 'string', required=True),
                             Field('event_name', 'string'),
                             Field('diadiem_tochuc', 'string'),
                             Field('thoigian_tochuc', 'datetime'),
                             Field('quan_huyen_tochuc', 'string'),
                             primarykey=['event_id', 'user_id'])

        if not self.db(self.db.orders).count():
            from gluon.contrib.populate import populate
            populate(self.db.orders, 25)

    def load_list_orders(self,start,end):
        listOrder = self.db(self.db.orders).select(orderby=self.db.orders.order_id, limitby=(start, end))
        return listOrder

    def get_all_order_id(self):
        return self.db().select(self.db.orders.order_id)

    def insert_orders(self,order_id,user_id,ngay_mua,name,event_name,age,phone,email,
                      cach_thanh_toan,phuong_thuc_nhan,quan_huyen):
        self.db.orders.insert(order_id=order_id, user_id=user_id, ngay_mua=ngay_mua,
                         name=name, event_name=event_name, age=age,
                         phone=phone, email=email, cach_thanh_toan=cach_thanh_toan,
                         phuong_thuc_nhan=phuong_thuc_nhan, quan_huyen=quan_huyen)

    def update_orders(self,order_id,user_id,ngay_mua,name,event_name,age,phone,email,
                      cach_thanh_toan,phuong_thuc_nhan,quan_huyen):
        self.db(self.db.orders.order_id == order_id).update(user_id=user_id,ngay_mua=ngay_mua,name=name,
                                                     event_name=event_name,age=age, phone=phone,
                                                    email=email,cach_thanh_toan=cach_thanh_toan,
                                                    phuong_thuc_nhan=phuong_thuc_nhan,quan_huyen=quan_huyen)

    def select_one_order(self,orderId):
        return self.db(self.db.orders.order_id == orderId).select(self.db.orders.ALL)

    def select_order_show(self,userId):
        return self.db(self.db.order_detail.user_id.like(userId)).select()

    def delete_order(self,orderId):
        self.db(self.db.orders.order_id == orderId).delete()