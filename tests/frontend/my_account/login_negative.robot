*** Settings ***
Library    SeleniumLibrary
Library    ../../../libraries/pages/MyAccountSignedOutPage.py    AS    my_acct



Test Setup          open browser            about:blank    ${BROWSER}
Test Teardown       close browser


*** Test Cases ***
Login none existing user
    [Tags]    tcid12    pioneertcid1    feregression    fesmoke    my_account


                        my_acct.go_to_my_account
                        my_acct.input_login_username    abcdef@supersqa.com
                        my_acct.input_login_password    abcdefg
                        my_acct.click_login_button

    ${expected_err}     set variable    Unknown email address. Check again or try your username
                        my_acct.wait_until_error_is_displayed    ${expected_err}


