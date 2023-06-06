

from libraries.configs.MainConfigs import MainConfigs
from libraries.pages.BasePage import BasePage



class MyAccountSignedOutPage(BasePage):

    endpoint = '/my-account/'
    LOGIN_USER_NAME = 'id:username'
    LOGIN_USER_PASSWORD = 'id:password'
    LOGIN_BTN = 'css:button.woocommerce-button[name="login"]'

    ERRORS_UL = 'css:ul.woocommerce-error'

    REGISTER_EMAIL = 'id:reg_email'
    REGISTER_PASSWORD = 'id:reg_password'
    REGISTER_BTN = 'css:button[name="register"][value="Register"]'


    def go_to_my_account(self):
        base_url = MainConfigs.get_base_url()
        my_account_url = base_url + self.endpoint
        self.bi.run_keyword("Go to", my_account_url)

    def input_login_username(self, username):
        self.bi.run_keyword("Wait until element is visible", self.LOGIN_USER_NAME)
        self.bi.run_keyword("Input text", self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.bi.run_keyword("Wait until element is visible", self.LOGIN_USER_PASSWORD)
        self.bi.run_keyword("Input text", self.LOGIN_USER_PASSWORD, password)

    def click_login_button(self):
        self.bi.run_keyword("Wait until element is visible", self.LOGIN_BTN)
        self.bi.run_keyword("Click element", self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.bi.run_keyword("Wait Until Element Contains", self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.bi.run_keyword("Wait until element is visible", self.LOGIN_BTN)
        self.bi.run_keyword("Input text", self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.bi.run_keyword("Wait until element is visible", self.REGISTER_PASSWORD)
        self.bi.run_keyword("Input text", self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.bi.run_keyword("Wait until element is visible", self.REGISTER_BTN)
        self.bi.run_keyword("Click element", self.REGISTER_BTN)
