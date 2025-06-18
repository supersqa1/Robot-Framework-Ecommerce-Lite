*** Settings ***
Documentation    Tests for the top banner showing message for Free Shipping. Banner exists in most pages but not all.
Library    SeleniumLibrary
Library    ../../../libraries/pages/HomePage.py
Library    ../../../libraries/pages/CartPage.py
Library    ../../../libraries/pages/CheckoutPage.py
Library    ../../../libraries/pages/components/NotificationBar.py
Library    ../../../libraries/pages/MyAccountSignedOutPage.py



Test Setup      open browser        about:blank    ${BROWSER}
Test Teardown   close browser



*** Test Cases ***
test_verify_free_shipping_banner_displayed_in_home_page(self)

    [Tags]    tcid69    notificationbar    feregression    fesmoke    example

        # go to home page
        HomePage.go_to_home_page

        # verify the notification bar is displayed
        NotificationBar.verify_notification_bar_is_displayed


test_verify_free_shipping_banner_displayed_in_cart_page

    [Tags]    tcid70    notificationbar    feregression    fesmoke    example

        # go to home page
        CartPage.go_to_cart_page

        # verify the notification bar is displayed
        NotificationBar.verify_notification_bar_is_displayed


test_verify_free_shipping_banner_displayed_in_checkout_page(self)

    [Tags]    tcid71    notificationbar    feregression    fesmoke    example

        HomePage.go_to_home_page
        HomePage.click_first_add_to_cart_button
        CheckoutPage.go_to_checkout_page

        # verify the notification bar is displayed
        NotificationBar.verify_notification_bar_is_displayed

test_verify_free_shipping_banner_not_displayed_in_my_account_page

    [Tags]    tcid72    notificationbar    feregression    fesmoke    example

        MyAccountSignedOutPage.go_to_my_account

        # verify the notification bar is not displayed
        NotificationBar.verify_notification_bar_is_not_displayed



