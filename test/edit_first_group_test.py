from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for edition"))
    old_groups = app.group.get_groups_list()
    group = Group("EditName","EditHeader","EditFooter");
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group;
    assert old_groups == new_groups;

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