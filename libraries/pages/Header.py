

# from pioneers_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
# from pioneers_store.src.pages.locators.HeaderLocators import HeaderLocators

from libraries.pages.BasePage import BasePage


class Header(BasePage):

    expected_menu_items = ['Home', 'Cart', 'Checkout', 'My account', 'Sample Page']
    CART_RIGHT_HEADER = 'id:site-header-cart'
    CART_ITEM_COUNT = 'css:li a.cart-contents span.count'
    MENU_ITEMS = 'css:div.menu ul.nav-menu li'

    def click_on_cart_on_right_header(self):
        self.sl.wait_until_element_is_visible(self.CART_RIGHT_HEADER)
        self.sl.click_element(self.CART_RIGHT_HEADER)

    def wait_until_cart_item_count(self, count):
        # expected_text = str(count) + ' item'
        expected_text = f'{str(count)} item'
        self.sl.wait_until_element_contains(self.CART_ITEM_COUNT, expected_text)

    def get_all_menu_item_text(self):
        # elms = self.sl.wait_and_get_elements(self.MENU_ITEMS)
        elms = self.bi.run_keyword("Get WebElements",self.MENU_ITEMS )
        # menu_text = []
        # for i in elms:
        #     menu_text.append(i.text)
        menu_text = [i.text for i in elms]
        return menu_text

    def assert_all_menu_items_displayed(self):
        displayed_menu_items = self.get_all_menu_item_text()

        for menu in self.expected_menu_items:
            self.bi.run_keyword("Should contain", displayed_menu_items, menu, f"Menu item '{menu}' is not displayed in the header.")
