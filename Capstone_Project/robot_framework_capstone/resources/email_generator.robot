*** Settings ***
Library    String

*** Keywords ***
Generate Unique Email
    ${random}    Generate Random String    4    0123456789
    ${email}     Set Variable    test_user_${random}@gmail.com

    # Store globally for suite (Register + Login)
    Set Suite Variable    ${EMAIL}    ${email}

    Log To Console    Dynamic Email Generated: ${EMAIL}
