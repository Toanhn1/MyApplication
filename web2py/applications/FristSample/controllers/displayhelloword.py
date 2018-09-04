#sample index page
from Validator import Validate
from StringMessage import Message as mess
from contact_orders import Connect
validate = Validate()
connect = Connect()
def index():
    return dict()

def allorder():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*10
    end = page*10
    listOrder = connect.load_list_orders(start,end)
    return dict(list = listOrder)

def addorder():
    order = request.vars.orderId
    listOrderId = connect.get_all_order_id()
    for row in listOrderId:
        if order in row.order_id :
            return redirect(URL("formadd",vars= dict(message=mess.error_key,message_email='', message_age='',message_date = '')))

    if not validate.isDate(request.vars.ngayMua):
        return redirect(URL("formadd", vars=dict(message_email='', message='', message_age='',message_date=mess.error_date)))

    if not validate.isAlnumric(request.vars.age):
        return redirect(URL("formadd", vars=dict(message_email='', message='',message_age = mess.error_age,message_date='')))

    if not validate.isEmail(request.vars.email):
        return redirect(URL("formadd", vars=dict(message_email=mess.error_email,message='',message_age='',message_date='')))

    connect.insert_orders(request.vars.orderId,request.vars.userId,request.vars.ngayMua,request.vars.name,
                request.vars.eventName,request.vars.age,request.vars.phone,request.vars.email,
                request.vars.cachThanhToan,request.vars.phuongThucNhan,request.vars.quanhuyen)

    return dict(id=request.vars.orderId)

def showdetail():
    userId = request.args[0]
    order_detail = connect.select_order_show(userId)
    return dict(list = order_detail)

def showupdate():
    orderId = request.vars.id
    order = connect.select_one_order(orderId)
    return dict(showOrder = order)

def doupdate():
    if not validate.isDate(request.vars.ngayMua):
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':mess.error_date,'message_age':'','message_email':''}))

    if not validate.isAlnumric(request.vars.age):
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':'','message_age':mess.error_age,'message_email':''}))

    if not validate.isEmail(request.vars.email):
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':'','message_age':'','message_email':mess.error_email}))

    connect.update_orders(request.vars.orderIdHiden,request.vars.userId,request.vars.ngayMua,
                          request.vars.name,request.vars.eventName,request.vars.age,request.vars.phone
                          ,request.vars.email,request.vars.cachThanhToan,request.vars.phuongThucNhan,request.vars.quanhuyen)

    return redirect(URL("allorder"))

def deleteorder():
    orderId = request.args[0]
    listOrderId = connect.get_all_order_id()
    for row in listOrderId:
        if not orderId in row.order_id:
            return redirect(URL("error"))
    connect.delete_order(orderId)
    return dict(idDel = orderId)

def formadd():
    return dict()

def error():
    return dict()