

def test_add_new_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first()
    app.session.logout()