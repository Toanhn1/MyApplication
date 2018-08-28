#sample index page
def index():
    listOrder = get_list_order()
    return dict(list = listOrder)

def get_list_order():
    return db().select(db.orders.ALL)