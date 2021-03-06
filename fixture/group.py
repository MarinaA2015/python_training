from model.group import Group

class GroupHelper:
    def __init__(self,app):
        self.app = app

    def return_to_group(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home(self):
        wd = self.app.wd
        if not(len(wd.find_elements_by_xpath("//a[contains(text(),'Last name')]"))>0):
            wd.find_element_by_link_text("home").click()

    def delete_first(self):
        self.delete_group_by_index(self,0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group()
        self.group_cache = None

    def edit_first(self, group):
        self.edit_group_by_index(self, group, 0)

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group changing
        wd.find_element_by_name("update").click()
        self.return_to_group()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group form
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def fill_field(self, field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        self.select_group_by_index(self, 0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group()
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for el in wd.find_elements_by_css_selector("span.group"):
                text = el.text
                id = el.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)



