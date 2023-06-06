
from libraries.pages.BasePage import BasePage


class MyAccountSignedInPage(BasePage):

    LEFT_NAV_LOGOUT_BTN = 'css:li.woocommerce-MyAccount-navigation-link--customer-logout a'

    def verify_user_is_signed_in(self):
        """
        Verifies user is signed in by checking the 'Log Out' button is visible
        on the left navigation bar.
        :return:
        """
        self.bi.run_keyword("Wait until element is visible", self.LEFT_NAV_LOGOUT_BTN)
