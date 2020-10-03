
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
        self.fill_field("firstname",contact.first_name)
        self.fill_field("lastname", contact.last_name)
        self.fill_field("company", contact.company)
        self.fill_field("home", contact.home_phone)


    def fill_field(self,name_field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(name_field).click()
            wd.find_element_by_name(name_field).clear()
            wd.find_element_by_name(name_field).send_keys(text)

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