
from libraries.pages.BasePage import BasePage



class OrderReceivedPage(BasePage):

    PAGE_MAIN_HEADER = 'css:header h1.entry-title'
    ORDER_NUMBER = 'css:li.order strong'


    def verify_order_received_page_loaded(self):
        # self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, "Order received")
        self.bi.run_keyword("Wait Until Element Contains", self.PAGE_MAIN_HEADER, "Order received")

    def get_order_number(self):
        # return self.sl.wait_and_get_text(self.ORDER_NUMBER)
        self.bi.run_keyword("Wait Until Element is visible", self.ORDER_NUMBER)
        return self.bi.run_keyword("Get Text", self.ORDER_NUMBER)
