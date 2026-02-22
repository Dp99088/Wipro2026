*** Settings ***
Resource   ../resources/common.robot
Resource   ../resources/locators.robot


*** Keywords ***

Open First Product Details

    # Assertion 1: Product Result is Visible
    Wait Until Element Is Visible    ${FIRST_PRODUCT}
    Element Should Be Visible        ${FIRST_PRODUCT}
    Element Should Be Enabled        ${FIRST_PRODUCT}

    # Step 1: Click First Product
    Click Element                    ${FIRST_PRODUCT}

    # Assertion 2: URL Changed to Product Page
    Location Should Contain          route=product

    # Step 2: Product Title Visible
    Wait Until Element Is Visible    ${PRODUCT_TITLE}
    Element Should Be Visible        ${PRODUCT_TITLE}

    # Assertion 3: Product Title is Not Empty
    ${title}=    Get Text    ${PRODUCT_TITLE}
    Should Not Be Empty      ${title}

    Log To Console    Product Details Page Opened Successfully!
    Log To Console    Opened Product: ${title}

    # Assertion 4: Add To Cart Button Exists (Next Scenario)
    Element Should Be Visible        ${ADD_TO_CART}
