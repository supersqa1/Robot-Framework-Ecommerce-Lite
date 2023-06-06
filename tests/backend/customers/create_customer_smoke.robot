*** Settings ***
Library    ../../../libraries/utilities/genericUtilities.py
Library    ../../../libraries/utilities/WooAPIUtility.py
Library    ../../../libraries/dao/CustomersDAO.py    AS    cust_dao




*** Test Cases ***
Create customer only email password

    [Tags]    tcid29    pioneertcid11    beregression    besmoke    customers_api    example


    # create payload with email and password only
    ${email_password}   genericUtilities.generate_random_email_and_password    email_prefix=pioneertcid11
    ${email}            set variable    ${email_password['email']}
    ${password}         set variable    ${email_password['password']}

                # make the call
    ${payload}  create dictionary    email=${email}    password=${password}
    ${rs_body}  WooAPIUtility.post    customers    params=${payload}    expected_status_code=201

                # verify response is good
                should not be empty    ${rs_body}    Response of create customers call should not be empty.
    ${check}    Evaluate                isinstance(${rs_body['id']}, int)
                should be true    ${check}    The id in response of create customer should be numeric."
                should be equal    ${email}    ${rs_body['email']}    Create customer endpoint email in response does not match in request
                  ...    Expected: {email}, Actual: {rs_body['email']}"
                should be equal    ${rs_body['role']}    customer    Create new customer API, customer role should be 'customer' but
                  ...    it was '{rs_body['role']}'

                # verify customer is created by checking the database
    ${db_info}  cust_dao.get_customer_by_email    ${email}
                log to console          ${db_info}
                length should be        ${db_info}    1    Expected 1 record for customer in 'users' table.
                should not be empty     ${db_info[0]['user_pass']}    After creating user with api, the password field in DB is empty.

    ${expected_display_name}    Evaluate    $email.split('@')[0]

    should be equal    ${db_info[0]['display_name']}    ${expected_display_name}    Display name database does not match expected." \
        ...    Email: {email}, Expected display: ${expected_display_name}
        ...    DB display name: ${db_info[0]['display_name']}

    should be equal    ${db_info[0]['user_login']}    ${expected_display_name}  user_login name database does not match expected." \
                            ...  Email: {email}, Expected display: {expected_display_name}" \
                            ...  DB display name: {db_info[0]['user_login']}"


Create customer fail for existing email

    [Tags]   tcid47    pioneertcid12    beregression    besmoke    customers_api    example

    # get random existing customer (from api or from db) - in this example we get it from db
    ${rand_cust}     cust_dao.get_random_customer_from_db
    ${rand_email}    set variable    ${rand_cust[0]['user_email']}

    log    Random email for the test: {rand_email}")    console=${true}

    # call api to create customer with the existing user
    ${email_password}    genericUtilities.generate_random_email_and_password    email_prefix=pioneertcid11
    ${random_password}   set variable    ${email_password['password']}
    ${payload}           create dictionary    email=${rand_email}    password=${random_password}

    ${rs_body}          WooAPIUtility.post    customers    params=${payload}  expected_status_code=400

    # verify the api response is a failure
    should be equal    ${rs_body['code']}    registration-error-email-exists    Create customer with existing user response does not
                                ...    have expected text. Expected: 'registration-error-email-exists', Actual: {${rs_body['code']}}

    should be equal as numbers    ${rs_body['data']['status']}  400    Unexpected status code in body of response.
                                     ...    Expected 400 actual: {${rs_body['data']['status']}}
    should contain   ${rs_body['message']}  An account is already registered with your email address.    Create customer with existing user
                            ...    response body 'message' did not contain expected text."

Create customer fail when no password is provided

    [Tags]   tcid32    pioneertcid13    beregression    besmoke    customers_api    example

    # get random email
    ${random_info}    genericUtilities.generate_random_email_and_password

    ${payload}  evaluate    {"email": $random_info["email"]}

    ${rs_api}   WooAPIUtility.post    wc_endpoint=customers    params=${payload}  expected_status_code=400
                log to console    ${rs_api}

                should be equal    ${rs_api['code']}  rest_missing_callback_param    The code field in response is not as expected.
                                                ...    Expected=rest_missing_callback_param' Actual= {${rs_api['code']}}
                should be equal    ${rs_api['message']}   Missing parameter(s): password    bad message in response

                should be equal as strings    ${rs_api['data']['params']}    ['password']
                should be equal as numbers    ${rs_api['data']['status']}    400

