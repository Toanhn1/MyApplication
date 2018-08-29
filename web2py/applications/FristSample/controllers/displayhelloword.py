#sample index page

def index():
    return dict()

def allorder():
    listOrder = db().select(db.orders.ALL)
    return dict(list = listOrder)

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
