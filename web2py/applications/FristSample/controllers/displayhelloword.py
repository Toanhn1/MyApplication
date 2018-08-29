#sample index page

def index():
    return dict()

def allorder():
    listOrder = db().select(db.orders.ALL)
    return dict(list = listOrder)

def formadd():
    return dict()

def addorder():
    db.orders.insert(order_id=request.vars.orderId, user_id=request.vars.userId, ngay_mua=request.vars.ngayMua,
                     name=request.vars.name,event_name=request.vars.eventName,age=request.vars.age,
                     phone=request.vars.phone, email=request.vars.email, cach_thanh_toan=request.vars.cachThanhToan,
                     phuong_thuc_nhan=request.vars.phuongThucNhan, quan_huyen=request.vars.quanhuyen)
    return dict(id=request.vars.orderId)

def showdetail():
    orderId = request.args[0]
    order_detail = db(db.order_detail.user_id.like(orderId)).select()
    return dict(list = order_detail)

def deleteorder():
    orderId = request.args[0]
    db(db.orders.order_id == orderId).delete()
    return dict(idDel = orderId)

def showhome():
    print("")
