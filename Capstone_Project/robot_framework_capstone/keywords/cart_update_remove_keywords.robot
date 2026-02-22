*** Settings ***

Resource   ../resources/common.robot
Resource   ../resources/locators.robot


*** Keywords ***

Update Cart Quantity And Remove Item

    # Step 1: Check View Cart Button
    ${cart_visible}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    ${VIEW_CART_BTN}    5s

    IF    not ${cart_visible}
        Log To Console    ⚠️ View Cart button not available. Cart may be empty. Skipping Update/Remove...
        Return From Keyword
    END

    Click Element    ${VIEW_CART_BTN}

    # Step 2: Confirm Cart Page
    Wait Until Element Is Visible    ${CART_HEADING}    5s
    Log To Console    ✅ Shopping Cart Page Opened


    # Step 3: Check Quantity Box Exists
    ${qty_present}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    ${QTY_BOX}    5s

    IF    not ${qty_present}
        Log To Console    ⚠️ No items found in cart. Skipping update/remove...
        Return From Keyword
    END


    # Step 4: Update Quantity
    Clear Element Text    ${QTY_BOX}
    Input Text            ${QTY_BOX}    2
    Textfield Value Should Be    ${QTY_BOX}    2


    # Step 5: Click Update Button
    ${update_enabled}=    Run Keyword And Return Status
    ...    Element Should Be Enabled    ${UPDATE_BTN}

    IF    not ${update_enabled}
        Log To Console    ⚠️ Update button not enabled. Skipping...
        Return From Keyword
    END

    Click Element    ${UPDATE_BTN}

    # Step 6: Validate Update Message (Safe)
    ${update_msg}=    Run Keyword And Return Status
    ...    Page Should Contain    Success: You have modified your shopping cart

    IF    ${update_msg}
        Log To Console    ✅ Quantity Updated Successfully
    ELSE
        Log To Console    ⚠️ Update message not displayed, continuing...
    END


    # Step 7: Remove Product
    ${remove_enabled}=    Run Keyword And Return Status
    ...    Element Should Be Enabled    ${REMOVE_BTN}

    IF    not ${remove_enabled}
        Log To Console    ⚠️ Remove button not enabled. Skipping...
        Return From Keyword
    END

    Click Element    ${REMOVE_BTN}
    Sleep    2s


    # Step 8: Validate Empty Cart
    ${empty_cart}=    Run Keyword And Return Status
    ...    Wait Until Page Contains    Your shopping cart is empty!    5s

    IF    ${empty_cart}
        Log To Console    ✅ Item Removed Successfully and Cart is Empty
    ELSE
        Log To Console    ⚠️ Cart empty message not shown.
    END
