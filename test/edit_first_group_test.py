from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for edition"))
    app.group.edit_first(Group("EditName","EditHeader","EditFooter"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for edition"))
    app.group.edit_first(Group(name="JustName"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for edition"))
    app.group.edit_first(Group(header="JustHeader"))