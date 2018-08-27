# ---- example index page ----
def index():
    from pydal import DAL, Field
    dbConnect = DAL('mysql://root:root@localhost/web2py2')
    try:
        dbConnect.define_table('list_event', Field('event_name', type='text'),
                               Field('dia_diem', type='text'),
                               Field('thoi_gian', type='date'),
                               )
        # dbConnect.list_event.insert(event_name='Phao Hoa', dia_diem='Cau rong', thoi_gian='2018/05/06')
        # dbConnect.list_event.insert(event_name='Cau phun lua', dia_diem='Cau rong', thoi_gian='2018/05/07')
        # dbConnect.list_event.insert(event_name='Duong pho', dia_diem='Hai Chau', thoi_gian='2018/05/06')

        getAllEvents = dbConnect().select(dbConnect.list_event.ALL)
    finally:
        if dbConnect:
            dbConnect.close()
    return dict(list=getAllEvents)
