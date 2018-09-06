#sample index page
from StringValidator import Validate
from string_error_message import Message as mess
from contact_orders import Connect
from attribute_list import Common as idx
from common_var import Regrex as regex
from screen_id import ScreenId as screen

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
        check = True
        list_check[idx.message_order] = mess.error_empty
    elif len(request.vars.orderId) > regex.max_lenhgt_id:
        check = True
        list_check[idx.message_order] = mess.error_lenght + str(regex.max_lenhgt_id)
    else:
        for row in listOrderId:
            if order in row.order_id:
                check = True
                list_check[idx.message_order] = mess.error_key

    if validate.isNotEmpty(request.vars.userId) == False:
        check = True
        list_check[idx.message_user] = mess.error_empty
    elif len(request.vars.userId) > regex.max_lenhgt_id:
        check = True
        list_check[idx.message_user] = mess.error_lenght + str(regex.max_lenhgt_id)

    if validate.isNotEmpty(request.vars.ngayMua) == False:
        check = True
        list_check[idx.message_ngaymua] = mess.error_empty
    elif not validate.isDate(request.vars.ngayMua):
        check = True
        list_check[idx.message_ngaymua] = mess.error_date

    if validate.isNotEmpty(request.vars.name) == False:
        check = True
        list_check[idx.message_name] = mess.error_empty

    if validate.isNotEmpty(request.vars.eventName) == False:
        list_check[idx.message_eventname] = mess.error_empty
        check = True
    elif len(request.vars.eventName) > regex.max_lenght_str :
        check = True
        list_check[idx.message_eventname] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.age) == False:
        list_check[idx.message_age] = mess.error_empty
        check = True
    elif not validate.isAlnumric(request.vars.age):
        list_check[idx.message_age] = mess.error_age
        check = True
    elif int(request.vars.age) < regex.min_age and int(request.vars.age) >regex.max_age:
        check = True
        list_check[idx.message_age] = mess.error_range_age

    if validate.isNotEmpty(request.vars.phone) == False:
        list_check[idx.message_phone] = mess.error_empty
        check = True
    elif len(request.vars.phone) > regex.max_number_phone:
        check = True
        list_check[idx.message_phone] = mess.error_lenght + str(regex.max_number_phone)

    if validate.isNotEmpty(request.vars.email) == False:
        check = True
        list_check[idx.message_email] = mess.error_empty
    elif not validate.isEmail(request.vars.email):
        check = True
        list_check[idx.message_email] = mess.error_email
    elif len(request.vars.email) > regex.max_lenght_str :
        check = True
        list_check[idx.message_email] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.cachThanhToan) == False:
        check = True
        list_check[idx.message_cachthanhtoan] = mess.error_empty
    elif len(request.vars.cachThanhToan) > regex.max_lenght_str :
        check = True
        list_check[idx.message_cachthanhtoan] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.phuongThucNhan) == False:
        check = True
        list_check[idx.message_phuongthucnhan] = mess.error_empty
    elif len(request.vars.phuongThucNhan) > regex.max_lenght_str :
        check = True
        list_check[idx.message_phuongthucnhan] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.quanhuyen) == False:
        check = True
        list_check[idx.message_quanhuyen] = mess.error_empty
    elif len(request.vars.quanhuyen) > regex.max_lenght_str :
        check = True
        list_check[idx.message_quanhuyen] = mess.error_lenght + str(regex.max_lenght_str)

    if check == True:
        return redirect(URL(screen.form_add, vars=list_check))
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
    check = False
    list_check = validate.list_vars(request.vars.orderIdHiden, request.vars.userId, request.vars.ngayMua,
                           request.vars.name, request.vars.eventName, request.vars.age, request.vars.phone,
                           request.vars.email, request.vars.cachThanhToan, request.vars.phuongThucNhan,
                           request.vars.quanhuyen)

    if validate.isNotEmpty(request.vars.userId) == False:
        check = True
        list_check[idx.message_user] = mess.error_empty
    elif len(request.vars.userId) > regex.max_lenhgt_id:
        check = True
        list_check[idx.message_user] = mess.error_lenght + str(regex.max_lenhgt_id)

    if validate.isNotEmpty(request.vars.ngayMua) == False:
        check = True
        list_check[idx.message_ngaymua] = mess.error_empty
    elif not validate.isDate(request.vars.ngayMua):
        check = True
        list_check[idx.message_ngaymua] = mess.error_date

    if validate.isNotEmpty(request.vars.name) == False:
        check = True
        list_check[idx.message_name] = mess.error_empty

    if validate.isNotEmpty(request.vars.eventName) == False:
        list_check[idx.message_eventname] = mess.error_empty
        check = True
    elif len(request.vars.eventName) > regex.max_lenght_str :
        check = True
        list_check[idx.message_eventname] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.age) == False:
        list_check[idx.message_age] = mess.error_empty
        check = True
    elif not validate.isAlnumric(request.vars.age):
        list_check[idx.message_age] = mess.error_age
        check = True
    elif int(request.vars.age) < regex.min_age and int(request.vars.age) >regex.max_age:
        check = True
        list_check[idx.message_age] = mess.error_range_age

    if validate.isNotEmpty(request.vars.phone) == False:
        list_check[idx.message_phone] = mess.error_empty
        check = True
    elif len(request.vars.phone) > regex.max_number_phone:
        check = True
        list_check[idx.message_phone] = mess.error_lenght + str(regex.max_number_phone)

    if validate.isNotEmpty(request.vars.email) == False:
        check = True
        list_check[idx.message_email] = mess.error_empty
    elif not validate.isEmail(request.vars.email):
        check = True
        list_check[idx.message_email] = mess.error_email
    elif len(request.vars.email) > regex.max_lenght_str :
        check = True
        list_check[idx.message_email] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.cachThanhToan) == False:
        check = True
        list_check[idx.message_cachthanhtoan] = mess.error_empty
    elif len(request.vars.cachThanhToan) > regex.max_lenght_str :
        check = True
        list_check[idx.message_cachthanhtoan] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.phuongThucNhan) == False:
        check = True
        list_check[idx.message_phuongthucnhan] = mess.error_empty
    elif len(request.vars.phuongThucNhan) > regex.max_lenght_str :
        check = True
        list_check[idx.message_phuongthucnhan] = mess.error_lenght + str(regex.max_lenght_str)

    if validate.isNotEmpty(request.vars.quanhuyen) == False:
        check = True
        list_check[idx.message_quanhuyen] = mess.error_empty
    elif len(request.vars.quanhuyen) > regex.max_lenght_str :
        check = True
        list_check[idx.message_quanhuyen] = mess.error_lenght + str(regex.max_lenght_str)

    if check == True:
        return redirect(URL(screen.show_update, vars=list_check))
    else:
        connect.update_orders(request.vars.orderIdHiden,request.vars.userId,request.vars.ngayMua,
                          request.vars.name,request.vars.eventName,request.vars.age,request.vars.phone
                          ,request.vars.email,request.vars.cachThanhToan,request.vars.phuongThucNhan,request.vars.quanhuyen)

        return redirect(URL(screen.all_order))

def deleteorder():
    orderId = request.args[0]
    listOrderId = connect.get_all_order_id()
    for rows in listOrderId:
        list_kq = rows
    if orderId in list_kq.order_id:
        connect.delete_order(orderId)
        return dict(idDel=orderId)
    else:
        return redirect(URL("error"))

def formadd():
    return dict()

def error():
    return dict()
