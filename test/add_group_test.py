# -*- coding: utf-8 -*-


from model.group import Group
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name-",10)]
#     for header in ["", random_string("header-",20)]
#     for footer in ["", random_string("footer-",20)]
# ]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name-",10), header=random_string("header-",20), footer=random_string("footer-",20))
    for i in range(5)
    ]

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
