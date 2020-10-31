from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//a[contains(text(),'Last name')]")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # return to home page
        self.open_home()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        #delete the element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # return to home page
        self.open_home()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        self.fill_contact_form(contact)
        #update the element
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # return to home page
        self.open_home()
        self.contact_cache = None


    def edit_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # edit the first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()


    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_xpath("//img[@title='Edit']"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for el in wd.find_elements_by_name("entry"):
                id = el.find_element_by_name("selected[]").get_attribute("value")
                first_name = el.find_element_by_xpath(".//td[3]").text
                last_name = el.find_element_by_xpath(".//td[2]").text
                all_phones = el.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                                                  all_phones_from_contact_page=all_phones))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        second_phone = wd.find_element_by_name("phone2").get_attribute("value")
        self.open_home()
        return Contact(id=id, first_name=first_name, last_name=last_name,  home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, second_phone=second_phone)



    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        second_phone = re.search("P: (.*)", text).group(1)
        self.open_home()
        return Contact(home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, second_phone=second_phone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
