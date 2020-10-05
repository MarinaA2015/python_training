from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for delete"))
    app.group.delete_first()
    app.group.return_to_home()