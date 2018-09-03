#sample index page
import re
from Common import Regrex as regex
def index():
    return dict()

def allorder():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*10
    end = page*10
    listOrder = db(db.orders).select(orderby=db.orders.order_id,limitby=(start,end))
    return dict(list = listOrder)

def addorder():
    errorKey = 'Duplicate entry '+request.vars.orderId+' for key PRIMARY'
    errorEmail = 'Plaer input right email format!'
    errorAge = 'Please input number!'
    errorDate = 'Please input MM-DD-YYYY!'
    order = request.vars.orderId
    listOrderId = db().select(db.orders.order_id)
    for row in listOrderId:
        if order in row.order_id :
            return redirect(URL("formadd",vars= dict(message=errorKey,message_email='', message_age='',message_date = '')))

    check_date = re.compile(regex.regrex_day)
    if not check_date.match(request.vars.ngayMua):
        return redirect(URL("formadd", vars=dict(message_email='', message='', message_age='',message_date = errorDate)))

    if not request.vars.age.isnumeric():
        return redirect(URL("formadd", vars=dict(message_email='', message='',message_age = errorAge,message_date='')))

    check_email = re.compile(regex.regrex_email)
    if not check_email.match(request.vars.email):
        return redirect(URL("formadd", vars=dict(message_email=errorEmail,message='',message_age='',message_date='')))

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
    orderId = request.vars.id
    order = db(db.orders.order_id == orderId).select(db.orders.ALL)
    return dict(showOrder = order)

def doupdate():
    errorEmail = 'Plaer input right email format!'
    errorAge = 'Please input number!'
    errorDate = 'Please input MM-DD-YYYY!'

    check_date = re.compile(regex.regrex_day)
    if not check_date.match(request.vars.ngayMua):
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':errorDate,'message_age':'','message_email':''}))

    if not request.vars.age.isnumeric():
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':'','message_age':errorAge,'message_email':''}))

    check_email = re.compile(regex.regrex_email)
    if not check_email.match(request.vars.email):
        return redirect(URL("showupdate",vars={'id':request.vars.orderIdHiden,'message_date':'','message_age':'','message_email':errorEmail}))

    db(db.orders.order_id == request.vars.orderIdHiden).update(user_id=request.vars.userId,ngay_mua=request.vars.ngayMua,
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

def formadd():
    return dict()

def error():
    return dict()