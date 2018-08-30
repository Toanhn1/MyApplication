#sample index page

def index():
    return dict()

def allorder():
    listOrder = db().select(db.orders.ALL)
    return dict(list = listOrder)

def formadd():
    return dict()

def addorder():
    error = 'Duplicate entry '+request.vars.orderId+' for key PRIMARY'
    order = request.vars.orderId
    listOrderId = db().select(db.orders.order_id)
    for row in listOrderId:
        if order in row.order_id :
            return redirect(URL("formadd",vars= dict(message=error)))
        else:
            db.orders.insert(order_id=request.vars.orderId, user_id=request.vars.userId, ngay_mua=request.vars.ngayMua,
                     name=request.vars.name,event_name=request.vars.eventName,age=request.vars.age,
                     phone=request.vars.phone, email=request.vars.email, cach_thanh_toan=request.vars.cachThanhToan,
                     phuong_thuc_nhan=request.vars.phuongThucNhan, quan_huyen=request.vars.quanhuyen)
            return dict(id=request.vars.orderId)

def showdetail():
    userId = request.args[0]
    order_detail = db(db.order_detail.user_id.like(userId)).select()
    return dict(list = order_detail)

def showupdate():
    orderId = request.args[0]
    order = db(db.orders.order_id == orderId).select(db.orders.ALL)
    return dict(showOrder = order)

def doupdate():
    error = 'Duplicate entry ' + request.vars.orderId + ' for key PRIMARY'
    order = request.vars.orderId
    listOrderId = db().select(db.orders.order_id)
    for row in listOrderId:
        if order in row.order_id:
            return redirect(URL("showupdate", vars=dict(message=error)))
        else:
            db(db.orders.order_id == request.vars.orderIdHiden).update(order_id=request.vars.orderId,
                                      user_id=request.vars.userId,ngay_mua=request.vars.ngayMua,
                                      name=request.vars.name,event_name=request.vars.eventName,
                                      age=request.vars.age,phone=request.vars.phone,
                                      email=request.vars.email,cach_thanh_toan=request.vars.cachThanhToan,
                                      phuong_thuc_nhan=request.vars.phuongThucNhan,
                                    quan_huyen=request.vars.quanhuyen)
            return redirect(URL("allorder"))

def deleteorder():
    orderId = request.args[0]
    db(db.orders.order_id == orderId).delete()
    return dict(idDel = orderId)

def abc():
    return 'error'
