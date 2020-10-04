

def test_delete_first_group(app):
    app.group.delete_first()
    app.group.return_to_home()