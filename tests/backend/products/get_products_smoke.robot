*** Settings ***
##Library    Browser
Library    SeleniumLibrary
#Library    ../../libraries/pages/HomePage.py
#Library    ../../libraries/pages/Header.py
##Library    ../libraries/pages/HomePage.HomePage
#Library    ../../libraries/pages/HomePage.py
#Library    ../../libraries/pages/Header.py
#Library    ../../libraries/pages/CartPage.py
#Library    ../../libraries/pages/MyAccountSignedOutPage.py
#Library    ../../libraries/pages/MyAccountSignedInPage.py
#Library    ../../libraries/utilities/genericUtilities.py
Library    ../../../libraries/utilities/WooAPIUtility.py
Library    ../../../libraries/api_helpers/ProductsAPIHelper.py
Library    ../../../libraries/dao/ProductsDAO.py
#Library    ../../libraries/dao/products_dao.py
#Library    ../../libraries/dao/products_dao.ProductsDAO.py
##Library    ../libraries/pages/HomePage.HomePage




#Test Setup    open browser    about:blank    ${BROWSER}
#Suite Teardown    close all browsers
#pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.home_page]


*** Variables ***
#${BROWSER}    CHROME

*** Test Cases ***
test_get_all_products_returns_not_empty
    [Tags]    tcid24    pioneertcid15    beregression    besmoke    products_api


    ${rs_api}    WooAPIUtility.get    products  expected_status_code=200
                 should not be empty    ${rs_api}    Get all products endpoint returned nothing.


test_end_to_end_checkout_guest_user
    [Tags]    tcid25    pioneertcid14    beregression    besmoke    products_api

    # get product that exists from db (also could have gotten it from api (list-products)
    ${rand_product}     ProductsDAO.get_random_product_from_db
    ${product_id}       set variable    ${rand_product[0]['ID']}
    ${product_name}     set variable    ${rand_product[0]['post_name']}

    ${product_title}    set variable    ${rand_product[0]['post_title']}
                        log    Test product id: {product_id}

    # make the api call
    ${rs_api}       ProductsAPIHelper.call_get_product_py_id    ${product_id}
                    should be equal as numbers  ${rs_api['id']}    ${product_id}    Get product call. Id in request does not match id in response
                    should be equal as strings    ${rs_api['slug']}    ${product_name}    'name mismatch'
                    should be equal as strings    ${rs_api['name']}  ${product_title}    'title mismatch'
