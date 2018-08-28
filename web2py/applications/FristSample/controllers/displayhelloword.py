
#sample index page
def index():
    listMember = db().select(db.members.ALL)
    return dict(list = listMember)