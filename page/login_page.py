import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction


class LoginPage(BaseAction):

    login_btn = By.ID, "com.netease.vopen:id/login_button"
    username_edit_text = By.ID, "com.netease.vopen:id/login_username"
    password_edit_text = By.ID, "com.netease.vopen:id/login_password"

    def is_login_btn_enabled(self):
        if "false" == self.find_element(self.login_btn).get_attribute("enabled"):
            return False
        return True

    def input_password(self, text):
        self.input_text(self.password_edit_text, text)

    def input_username(self, text):
        self.input_text(self.username_edit_text, text)

    def click_login_btn(self):
        self.click(self.login_btn)