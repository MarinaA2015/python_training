# -*- coding: utf-8 -*-


from model.group import Group
import pytest
from data.add_group import constant as testdata


@pytest.mark.parametrize("group", testdata,ids=[repr(x) for x in testdata])
def test_add_new_group(app,group):
    old_groups = app.group.get_groups_list()
    #group_new = Group("GroupName", "GroupHeader", "GroupFooter")
    app.group.create(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups)+1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.group.open_home()


# def test_empty_group(app):
#
#     old_groups = app.group.get_groups_list()
#     #group_new = Group("", "", "")
#     app.group.create(group_new)
#     new_groups = app.group.get_groups_list()
#     app.group.open_home()
#     assert len(old_groups) + 1 == app.group.count()
#     old_groups.append(group_new)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     app.group.open_home()
