*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://practicetestautomation.com/practice-test-login/
${BROWSER}    chrome
${USERNAME}   student
${PASSWORD}   Password123

*** Test Cases ***
Verify Successful Login Using BuiltIn Keywords
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Text box interaction
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}

    Sleep    2s

    # Form submission
    Click Button    id=submit

    # Validation
    Wait Until Page Contains    Logged In Successfully    10s

    ${actual_url}=    Get Location
    ${expected_url}=  Set Variable    https://practicetestautomation.com/logged-in-successfully/

    Should Be Equal    ${actual_url}    ${expected_url}

    Run Keyword If    '${actual_url}'=='${expected_url}'    Log    Login Successful

    Close Browser
