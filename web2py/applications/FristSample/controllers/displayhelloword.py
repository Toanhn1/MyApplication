#sample index page
from StringValidator import Validate
from StringMessages import Message as mess
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
    check = False
    list_check = validate.list_vars(request.vars.orderId,request.vars.userId,request.vars.ngayMua,
                            request.vars.name,request.vars.eventName,request.vars.age,request.vars.phone,
                            request.vars.email,request.vars.cachThanhToan,request.vars.phuongThucNhan,request.vars.quanhuyen)

    if validate.isNotEmpty(request.vars.orderId) == False:
        list_check['message_order'] = mess.error_empty
    else:
        for row in listOrderId:
            if order in row.order_id:
                check = True
                list_check['message_order'] = mess.error_key

    if validate.isNotEmpty(request.vars.userId) == False:
        list_check['message_user'] = mess.error_empty

    if validate.isNotEmpty(request.vars.ngayMua) == False:
        list_check['message_ngaymua'] = mess.error_empty
    elif not validate.isDate(request.vars.ngayMua):
        list_check['message_ngaymua'] = mess.error_date

    if validate.isNotEmpty(request.vars.name) == False:
        list_check['message_name'] = mess.error_empty

    if validate.isNotEmpty(request.vars.eventName) == False:
        list_check['message_eventname'] = mess.error_empty

    if validate.isNotEmpty(request.vars.age) == False:
        list_check['message_age'] = mess.error_empty
    elif not validate.isAlnumric(request.vars.age):
        list_check['message_age'] = mess.error_age

    if validate.isNotEmpty(request.vars.phone) == False:
        list_check['message_phone'] = mess.error_empty

    if validate.isNotEmpty(request.vars.email) == False:
        list_check['message_email'] = mess.error_empty
    elif not validate.isEmail(request.vars.email):
        list_check['message_email'] = mess.error_email

    if validate.isNotEmpty(request.vars.cachThanhToan) == False:
        list_check['message_cachthanhtoan'] = mess.error_empty

    if validate.isNotEmpty(request.vars.phuongThucNhan) == False:
        list_check['message_phuongthucnhan'] = mess.error_empty

    if validate.isNotEmpty(request.vars.quanhuyen) == False:
        list_check['message_quanhuyen'] = mess.error_empty

    if any( [validate.isNotEmpty(request.vars.orderId) == False,validate.isNotEmpty(request.vars.userId) == False,
             validate.isNotEmpty(request.vars.ngayMua) == False,validate.isNotEmpty(request.vars.name) == False,
             validate.isNotEmpty(request.vars.eventName) == False,validate.isNotEmpty(request.vars.age) == False,
             validate.isNotEmpty(request.vars.phone) == False,validate.isNotEmpty(request.vars.email) == False,
             validate.isNotEmpty(request.vars.cachThanhToan) == False,validate.isNotEmpty(request.vars.phuongThucNhan) == False,
             validate.isNotEmpty(request.vars.quanhuyen) == False,check == True,not validate.isDate(request.vars.ngayMua),
             not validate.isAlnumric(request.vars.age),not validate.isEmail(request.vars.email)]):
        return redirect(URL("formadd", vars=list_check))
    else:
        connect.insert_orders(request.vars.orderId,request.vars.userId,request.vars.ngayMua,request.vars.name,
                    request.vars.eventName,request.vars.age,request.vars.phone,request.vars.email,
                    request.vars.cachThanhToan,request.vars.phuongThucNhan,request.vars.quanhuyen)
    return dict(id=request.vars.orderId)

def showdetail():
    userId = request.args[0]
    order_detail = connect.select_order_show(userId)
    return dict(list = order_detail)

def showupdate():
    return dict()

def doupdate():
    list_check = validate.list_vars(request.vars.orderIdHiden, request.vars.userId, request.vars.ngayMua,
                           request.vars.name, request.vars.eventName, request.vars.age, request.vars.phone,
                           request.vars.email, request.vars.cachThanhToan, request.vars.phuongThucNhan,
                           request.vars.quanhuyen)

    if validate.isNotEmpty(request.vars.userId) == False:
        list_check['message_user'] = mess.error_empty

    if validate.isNotEmpty(request.vars.ngayMua) == False:
        list_check['message_ngaymua'] = mess.error_empty
    elif not validate.isDate(request.vars.ngayMua):
        list_check['message_ngaymua'] = mess.error_date

    if validate.isNotEmpty(request.vars.name) == False:
        list_check['message_name'] = mess.error_empty

    if validate.isNotEmpty(request.vars.eventName) == False:
        list_check['message_eventname'] = mess.error_empty

    if validate.isNotEmpty(request.vars.age) == False:
        list_check['message_age'] = mess.error_empty
    elif not validate.isAlnumric(request.vars.age):
        list_check['message_age'] = mess.error_age

    if validate.isNotEmpty(request.vars.phone) == False:
        list_check['message_phone'] = mess.error_empty

    if validate.isNotEmpty(request.vars.email) == False:
        list_check['message_email'] = mess.error_empty
    elif not validate.isEmail(request.vars.email):
        list_check['message_email'] = mess.error_email

    if validate.isNotEmpty(request.vars.cachThanhToan) == False:
        list_check['message_cachthanhtoan'] = mess.error_empty

    if validate.isNotEmpty(request.vars.phuongThucNhan) == False:
        list_check['message_phuongthucnhan'] = mess.error_empty

    if validate.isNotEmpty(request.vars.quanhuyen) == False:
        list_check['message_quanhuyen'] = mess.error_empty

    if any( [validate.isNotEmpty(request.vars.userId) == False,validate.isNotEmpty(request.vars.ngayMua) == False,
             validate.isNotEmpty(request.vars.name) == False,validate.isNotEmpty(request.vars.eventName) == False,
             validate.isNotEmpty(request.vars.age) == False,not validate.isEmail(request.vars.email),
             validate.isNotEmpty(request.vars.phone) == False,validate.isNotEmpty(request.vars.email) == False,
             validate.isNotEmpty(request.vars.cachThanhToan) == False,validate.isNotEmpty(request.vars.phuongThucNhan) == False,
             validate.isNotEmpty(request.vars.quanhuyen) == False,not validate.isDate(request.vars.ngayMua),
             not validate.isAlnumric(request.vars.age)]):
        return redirect(URL("", vars=list_check))
    else:
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
