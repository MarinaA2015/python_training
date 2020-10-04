from model.group import Group


def test_edit_first_group(app):

    app.group.edit_first(Group("EditName","EditHeader","EditFooter"))

def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="JustName"))

def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="JustHeader"))