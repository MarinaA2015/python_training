from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for edition"))
    old_groups = app.group.get_groups_list()
    group = Group("EditName", "EditHeader", "EditFooter");
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group;
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max);

#def test_edit_first_group_name(app):
 #   if app.group.count() == 0:
 #       app.group.create(Group(name="for edition"))
 #   old_groups = app.group.get_groups_list()
#  app.group.edit_first(Group(name="JustName"))
  #  new_groups = app.group.get_groups_list()
  #  assert len(old_groups) == len(new_groups)

#def test_edit_first_group_header(app):
   # if app.group.count() == 0:
   #     app.group.create(Group(name="for edition"))
   #old_groups = app.group.get_groups_list()
   # app.group.edit_first(Group(header="JustHeader"))
   # new_groups = app.group.get_groups_list()
   # assert len(old_groups) == len(new_groups)