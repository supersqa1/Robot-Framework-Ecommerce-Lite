

# from pioneers_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
# from pioneers_store.src.pages.CartPageLocators import CartPageLocators
# from pioneers_store.src.pages.locators.CartPageLocators import CartPageLocators
from libraries.configs.MainConfigs import MainConfigs
from libraries.pages.BasePage import BasePage
# import sys, pdb;

# pdb.Pdb(stdout=sys.__stdout__).set_trace()

class CartPage(BasePage):

    endpoint = '/cart'

    PRODUCT_NAMES_IN_CART = 'css:tr.cart_item td.product-name'

    COUPON_FIELD = 'id:coupon_code'
    APPLY_COUPON_BTN = 'css:button[name="apply_coupon"]'

    PROCEED_TO_CHECKOUT_BTN = 'css:a.checkout-button'


    def go_to_cart_page(self):
        base_url = MainConfigs.get_base_url()
        cart_url = base_url + self.endpoint
        self.bi.run_keyword("Go to", cart_url)

    def get_all_product_names_in_cart(self):

        self.bi.run_keyword("Wait until element is visible", self.PRODUCT_NAMES_IN_CART)
        product_name_elements = self.bi.run_keyword("Get webelements", self.PRODUCT_NAMES_IN_CART)

        product_names = [i.text for i in product_name_elements]
        # product_names = []
        # for i in product_name_elements:
        #     product_names.append(i.text)
        return product_names

    def input_coupon(self, coupon_code):
        # self.sl.wait_and_input_text(self.COUPON_FIELD, str(coupon_code))
        self.bi.run_keyword("Wait until element is visible", self.COUPON_FIELD)
        self.bi.run_keyword("Input Text", self.COUPON_FIELD, str(coupon_code))

    def click_apply_coupon(self):
        # self.sl.wait_and_click(self.APPLY_COUPON_BTN)
        self.bi.run_keyword("Wait until element is visible", self.APPLY_COUPON_BTN)
        self.bi.run_keyword("Click element", self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

    def click_on_proceed_to_checkout(self):
        # self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)
        self.bi.run_keyword("Wait until element is visible", self.PROCEED_TO_CHECKOUT_BTN)
        self.bi.run_keyword("Click element", self.PROCEED_TO_CHECKOUT_BTN)
