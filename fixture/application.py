from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def isValid(self):
        try:
            self.wd.current_url
            return  True
        except:
            return  False

    def open_application(self):
        wd = self.wd
        # open application
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()