
from libraries.pages.BasePage import BasePage
from libraries.configs.MainConfigs import MainConfigs
from libraries.utilities.genericUtilities import generate_random_email_and_password


# from pioneers_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
# from libraries.utilities.genericUtilities import generate_random_email_and_password

class CheckoutPage(BasePage):

    endpoint = '/checkout'
    BILLING_FIRST_NAME_FIELD = 'id:billing_first_name'
    BILLING_LAST_NAME_FIELD = 'id:billing_last_name'
    BILLING_ADDRESS_1_FIELD = 'id:billing_address_1'
    BILLING_CITY_FIELD = 'id:billing_city'
    BILLING_ZIP_FIELD = 'id:billing_postcode'
    BILLING_PHONE_FIELD = 'id:billing_phone'
    BILLING_EMAIL_FIELD = 'id:billing_email'
    BILLING_COUNTRY_DROPDOWN = 'id:billing_country'
    BILLING_STATE_DROPDOWN = 'id:billing_state'

    PLACE_ORDER_BTN = 'id:place_order'

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.sl = SeleniumExtended(driver)

    def go_to_checkout_page(self):
        base_url = MainConfigs.get_base_url()
        checkout_url = base_url + self.endpoint
        self.bi.run_keyword("Go to", checkout_url)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFname'
        self.bi.run_keyword("Wait until element is visible", self.BILLING_FIRST_NAME_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_FIRST_NAME_FIELD, str(first_name))

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'AutomationLname'
        self.bi.run_keyword("Wait until element is visible", self.BILLING_LAST_NAME_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_LAST_NAME_FIELD, str(last_name))

    def input_billing_street_address_1(self, address1=None):
        address1 = address1 if address1 else "123 Main st."
        self.bi.run_keyword("Wait until element is visible", self.BILLING_ADDRESS_1_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_ADDRESS_1_FIELD, str(address1))

    def input_billing_city(self, city=None):
        city = 'San Francisco' if not city else city
        self.bi.run_keyword("Wait until element is visible", self.BILLING_CITY_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_CITY_FIELD, str(city))

    def input_billing_zip(self,  zip_code=None):
        zip_code = 94016 if not zip_code else zip_code
        self.bi.run_keyword("Wait until element is visible", self.BILLING_ZIP_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_ZIP_FIELD, str(zip_code))

    def input_billing_phone_number(self, phone=None):
        phone = '4151111111' if not phone else phone
        self.bi.run_keyword("Wait until element is visible", self.BILLING_PHONE_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_PHONE_FIELD, str(phone))

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.bi.run_keyword("Wait until element is visible", self.BILLING_EMAIL_FIELD)
        self.bi.run_keyword("Input Text", self.BILLING_EMAIL_FIELD, str(email))

    def select_billing_country(self, country=None):
        country = 'United States (US)' if not country else country
        # self.sl.wait_and_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by="visible_text")
        self.bi.run_keyword("Wait until element is visible", self.BILLING_COUNTRY_DROPDOWN)
        self.bi.run_keyword("Select From List By Label", self.BILLING_COUNTRY_DROPDOWN, str(country))

    def select_billing_state(self, state=None):
        state = 'California' if not state else state
        # self.sl.wait_and_select_dropdown(self.BILLING_STATE_DROPDOWN, to_select=state, select_by="visible_text")
        self.bi.run_keyword("Wait until element is visible", self.BILLING_STATE_DROPDOWN)
        self.bi.run_keyword("Select From List By Label", self.BILLING_STATE_DROPDOWN, str(state))

    def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, city=None, zip_code=None, phone=None, email=None, state=None, country=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address_1(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip_code=zip_code)
        self.input_billing_phone_number(phone=phone)
        self.input_billing_email(email=email)
        self.select_billing_country(country)
        self.select_billing_state(state=state)

    def click_place_order(self):
        self.bi.run_keyword("Wait until element is visible", self.PLACE_ORDER_BTN)
        self.bi.run_keyword("Click element", self.PLACE_ORDER_BTN)
