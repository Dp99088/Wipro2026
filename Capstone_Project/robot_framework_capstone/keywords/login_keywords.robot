*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/common.robot
Resource   ../resources/locators.robot


*** Keywords ***

Login User Successfully
    [Arguments]    ${password}
    # Step 0: Open Home Page
    Go To    ${BASE_URL}

    Page Should Contain    My account

    # Step 1: Click My Account Dropdown
    Wait Until Element Is Visible    ${MY_ACCOUNT_MENU}
    Click Element                    ${MY_ACCOUNT_MENU}
    Sleep    1s

    # Step 2: Click Login Option
    Wait Until Element Is Visible    ${LOGIN_LINK}
    Click Element                    ${LOGIN_LINK}

    # Assertion: Login Page Loaded
    Wait Until Page Contains         Account Login
    Location Should Contain          route=account/login

    # Step 3: Enter Credentials
    Log To Console    Logging in with Email: ${EMAIL}

    Input Text    ${EMAIL_INPUT}       ${EMAIL}
    Input Text    ${PASSWORD_INPUT}    ${password}

    # Step 4: Click Login Button
    Click Button    ${LOGIN_BUTTON}

    # Step 5: Validate Login Success
    Wait Until Page Contains          My Account
    Wait Until Element Is Visible     ${MY_ACCOUNT_HEADING}

    Page Should Contain              My Account
    Location Should Contain          route=account/account

    Log To Console    Login Successful After Logout

