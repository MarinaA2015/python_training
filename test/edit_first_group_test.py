from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first(Group("EditName","EditHeader","EditFooter"))
    app.session.logout()

def test_edit_first_group_name(app):
    app.session.login("admin","secret")
    app.group.edit_first(Group(name="JustName"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login("admin","secret")
    app.group.edit_first(Group(header="JustHeader"))
    app.session.logout()