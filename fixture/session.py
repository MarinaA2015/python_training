from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_application()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        #wd.find_element_by_link_text("Logout").click()
        wd.implicitly_wait(5)
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_link_text("Logout").click()
        #logout_button = WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        #logout_button.click();
        #wd.find_element_by_xpath("//form[@name='logout']/a").click()