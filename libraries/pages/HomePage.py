


from robot.api import logger
from libraries.pages.BasePage import BasePage
from libraries.configs.MainConfigs import MainConfigs


class HomePage(BasePage):

    ADD_TO_CART_BTN = 'css:li.product a.button.add_to_cart_button'
    PRODUCT = 'css:ul.products li.product'
    PAGE_HEADING = 'css:header.woocommerce-products-header h1.page-title'


    def go_to_home_page(self):
        base_url = MainConfigs.get_base_url()
        # self.sl.go_to(base_url)
        self.bi.run_keyword("Go to", base_url)

    def click_first_add_to_cart_button(self):
        self.bi.run_keyword("wait until element is visible", self.ADD_TO_CART_BTN)
        return self.bi.run_keyword("Click element", self.ADD_TO_CART_BTN)

    def get_number_of_products_displayed(self):
        return self.bi.run_keyword("Get Element Count", self.PRODUCT) #(self.PRODUCT, err=error_msg)
        # self.bi.run_keyword("wait until element is visible", self.PRODUCT)
        # elems = self.bi.run_keyword("Get WebElements", self.PRODUCT)
        # return len(elems)

    def get_all_product_elements(self):
        error_msg = "Can not get product elements from home page."

        # products_elm = self.sl.wait_and_get_elements(self.PRODUCT, err=error_msg)
        # return products_elm

        self.bi.run_keyword("wait until element is visible", self.PRODUCT) #(self.PRODUCT, err=error_msg)
        return self.bi.run_keyword("Get WebElements", self.PRODUCT) #(self.PRODUCT, err=error_msg)
        # return self.sl.wait_and_get_elements(self.PRODUCT, err=error_msg)

    def get_displayed_heading(self):
        # return self.sl.wait_and_get_text(self.PAGE_HEADING)
        self.bi.run_keyword("wait until element is visible", self.PAGE_HEADING)
        return self.bi.run_keyword("get text", self.PAGE_HEADING)
