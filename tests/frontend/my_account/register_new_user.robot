*** Settings ***
Library    SeleniumLibrary
Library    ../../../libraries/pages/MyAccountSignedOutPage.py
Library    ../../../libraries/pages/MyAccountSignedInPage.py
Library    ../../../libraries/utilities/genericUtilities.py

Test Setup      open browser    about:blank    ${BROWSER}
Suite Teardown  close all browsers


*** Test Cases ***
test_register_valid_new_user
    [Tags]    tcid13    feregression    fesmoke    my_account

        # go to my account page
        MyAccountSignedOutPage.go_to_my_account

        ${random_info}    genericUtilities.generate_random_email_and_password
                          log to console    ${random_info}

        # fill in the username for registration
        MyAccountSignedOutPage.input_register_email    ${random_info['email']}

        # fill in the password for registration
        MyAccountSignedOutPage.input_register_password    ${random_info['password']}

        # click on 'register'
        MyAccountSignedOutPage.click_register_button

        # verify user is registered
        MyAccountSignedInPage.verify_user_is_signed_in
