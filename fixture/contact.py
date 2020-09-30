
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # return to home page
        self.return_to_home()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)

    def delete_first(self):
        wd = self.app.wd
        self.edit_first_contact()
        #delete the element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # return to home page
        self.return_to_home()

    def edit_first(self,contact):
        wd = self.app.wd
        self.edit_first_contact()
        self.fill_contact_form(contact)
        #update the element
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # return to home page
        self.return_to_home()

    def edit_first_contact(self):
        wd = self.app.wd
        # edit the first cotact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()