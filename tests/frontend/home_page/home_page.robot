*** Settings ***
Library    SeleniumLibrary
Library    ../../../libraries/pages/HomePage.py
Library    ../../../libraries/pages/Header.py

Test Setup        open browser and go to home page
Suite Teardown    close all browsers


*** Variables ***
${expected_number_of_products}     12


*** Test Cases ***
test_verify_number_of_products_displayed
    [Tags]    tcid1    pioneertcid4    feregression    fesmoke    home_page    example

                            HomePage.go to home page
    ${displayed_products}   HomePage.get_number_of_products_displayed
                            builtin.should be equal as integers    ${displayed_products}    ${expected_number_of_products}

        # Example: another way to validate
    #    ${displayed_products}     HomePage.get_all_product_elements
    #                              builtin.length should be          ${displayed_products}    ${expected_number_of_products}


test_verify_heading_is_displayed
    [Tags]    tcid67    pioneertcid5    feregression    fesmoke    home_page    example

        ${expected_heading}     set variable    Shop

        ${displayed_heading}    HomePage.Get displayed heading

        should be equal as strings    ${expected heading}    ${displayed_heading}
        ...    msg=Displayed heading in home page is not as expected. Expected: ${expected_heading}, Actual: ${displayed_heading}"


test_verify_header_menu_is_displayed:
    [Tags]    tcid4    pioneertcid6        feregression    fesmoke    home_page    example

        Header.assert_all_menu_items_displayed


*** Keywords ***
open browser and go to home page
    SeleniumLibrary.open browser    about:blank    browser=${BROWSER}
    go to home page


