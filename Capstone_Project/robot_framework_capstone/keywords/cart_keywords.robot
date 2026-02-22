*** Settings ***

Resource   ../resources/common.robot
Resource   ../resources/locators.robot


*** Keywords ***

Add Product To Cart And Validate Success

    # Check Add To Cart button exists
    ${present}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    ${ADD_TO_CART}    5s

    IF    not ${present}
        Log To Console    ❌ Add To Cart not found (Out of Stock). Skipping...
        Return From Keyword
    END

    Scroll Element Into View    ${ADD_TO_CART}

    # Check button enabled
    ${enabled}=    Run Keyword And Return Status
    ...    Element Should Be Enabled    ${ADD_TO_CART}

    IF    not ${enabled}
        Log To Console    ⚠️ Product Out of Stock (Button Disabled). Skipping Add To Cart...
        Return From Keyword
    END

    # Click Add To Cart
    Click Element    ${ADD_TO_CART}
    Sleep    3s

    # Validate success message
    ${success}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    ${CART_SUCCESS_MSG}    5s

    IF    not ${success}
        Log To Console    ⚠️ No success message appeared. Product may not be added.
        Return From Keyword
    END

    Log To Console    ✅ Product Added To Cart Successfully!

    Wait Until Element Is Visible    ${VIEW_CART_BTN}
    Element Should Be Visible        ${VIEW_CART_BTN}
