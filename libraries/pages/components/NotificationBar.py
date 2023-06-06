

# from libraries.selenium_extended.SeleniumExtended import SeleniumExtended
from libraries.pages.BasePage import BasePage




class NotificationBar(BasePage):

    NOTIFICATION_BAR_TEXT = 'css:div#wpfront-notification-bar table#wpfront-notification-bar-table div.wpfront-message strong'

    # def __init__(self, driver):
    #     self.sl = SeleniumExtended(driver)

    def verify_notification_bar_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.NOTIFICATION_BAR_TEXT)

    def verify_notification_bar_is_not_displayed(self):

        try:
            self.sl.wait_until_element_is_visible(self.NOTIFICATION_BAR_TEXT, timeout=3)
            raise Exception(f"The 'Notification Bar' should not be displayed but it is displayed.")
        except:
            print("Banner is not displayed.")

