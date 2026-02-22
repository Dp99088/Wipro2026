*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/common.robot
Resource   ../resources/locators.robot
Resource   ../resources/email_generator.robot
Resource   ../keywords/logout_keywords.robot


*** Keywords ***

Register New User

    # Open Home Page
    Go To    ${BASE_URL}

    # Assertion 1: Home Page Loaded
    Title Should Be    Your Store
    Page Should Contain    My account

    # Step 1: Click My Account Dropdown
    Wait Until Element Is Visible    ${MY_ACCOUNT_MENU}
    Click Element                    ${MY_ACCOUNT_MENU}
    Sleep    1s

    # Step 2: Click Register Option
    Wait Until Element Is Visible    ${REGISTER_LINK}
    Click Element                    ${REGISTER_LINK}

    # Assertion 2: Register Page Loaded
    Wait Until Page Contains         Register Account
    Location Should Contain          route=account/register



# Fill Registration Form using CSV Data
input firstname
    [Arguments]    ${firstname}

    Input Text    ${FIRSTNAME_INPUT}    ${firstname}
input lastname
    [Arguments]    ${lastname}
    Input Text    ${LASTNAME_INPUT}     ${lastname}
input email
    # Generate Unique Email for Every Row
    Generate Unique Email
    Log To Console    Registering with Email: ${EMAIL}
    Input Text    ${EMAIL_INPUT}        ${EMAIL}
input phone
    [Arguments]    ${phone}
    Input Text    ${PHONE_INPUT}        ${phone}
input password
    [Arguments]    ${password}
    Input Text    ${PASSWORD_INPUT}     ${password}
    Input Text    ${CONFIRM_INPUT}      ${password}

    # Assertion 3: Password Match
    Textfield Value Should Be        ${CONFIRM_INPUT}    ${password}

click agree
    # Agree Terms
    Click Element    ${AGREE_LABEL}
    Checkbox Should Be Selected      id=input-agree
click continue
    # Submit Form
    Scroll Element Into View    ${CONTINUE_BUTTON}
    Click Button               ${CONTINUE_BUTTON}

    # Assertion 4: Registration Success
    Wait Until Element Is Visible    ${SUCCESS_TEXT}
    Page Should Contain              Your Account Has Been Created

    Log To Console    Registration Completed Successfully for ${firstname}
click logout
    # Logout After Registration
    Logout User Successfully
