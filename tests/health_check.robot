*** Settings ***
Library    SeleniumLibrary
Library    ../libraries/pages/HomePage.py



*** Test Cases ***
Create Quote for Car
    [Tags]    healthcheck

    Open browser    about:blank     browser=${BROWSER}
    HomePage.go to home page

