# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group(app):
    #app.session.login("admin", "secret")
    app.group.create(Group("GroupName", "GroupHeader", "GroupFooter"))
    app.group.return_to_home()
    #app.session.logout()

def test_empty_group(app):
   app.group.create(Group("", "", ""))
   app.group.return_to_home()