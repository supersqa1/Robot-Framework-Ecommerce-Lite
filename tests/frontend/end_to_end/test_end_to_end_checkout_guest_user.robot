*** Settings ***
Documentation    End-to-end flow of ordering a product as a guest user. User does not sign in
...    but adds to item to cart and completes the checkout process.

Library    SeleniumLibrary
Library    ../../../libraries/configs/MainConfigs.py
Library    ../../../libraries/pages/HomePage.py
Library    ../../../libraries/pages/Header.py
Library    ../../../libraries/pages/CheckoutPage.py
Library    ../../../libraries/pages/OrderReceivedPage.py
Library    ../../../libraries/pages/CartPage.py
Library    ../../../libraries/utilities/WooAPIUtility.py



Test Setup      open browser    about:blank    ${BROWSER}
Test Teardown   close browser


*** Test Cases ***
End to end checkout guest user
    [Tags]    tcid33    feregression    fesmoke    home_page    example

                            # go to home page
                            HomePage.go_to_home_page

                            # add item to cart
                            HomePage.click_first_add_to_cart_button

                            # make sure the cart is updated before going to cart
                            Header.wait_until_cart_item_count    1


                            # go to cart
                            Header.click_on_cart_on_right_header

                            # verify there are items in the cart
        ${product_names}    CartPage.get_all_product_names_in_cart
                            length should be    ${product_names}    1

                            #  apply coupon
        ${coupon_code}      MainConfigs.get_coupon_code    FREE_COUPON
                            CartPage.apply_coupon    ${coupon_code}

                            # proceed to checkout
                            CartPage.click_on_proceed_to_checkout

                            # fill in checkout form
                            CheckoutPage.fill_in_billing_info

                            # submit
                            CheckoutPage.click_place_order

                            # verify order is placed
                            OrderReceivedPage.verify_order_received_page_loaded
        ${order_number}     OrderReceivedPage.get order number

        ${order_api}        WooAPIUtility.get    orders/${order_number}     expected_status_code=200
                            should be equal as numbers    ${order_api['id']}    ${order_number}
