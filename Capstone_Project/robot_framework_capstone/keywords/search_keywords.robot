*** Settings ***
Resource   ../resources/common.robot
Resource   ../resources/locators.robot


*** Keywords ***

Search Products

    # Step 0: Open Home Page
    Go To    ${BASE_URL}

    # Assertion 1: Home Page Loaded
    Location Should Contain    index.php
    Page Should Contain        Search


    # Step 1: Search Box Visible
    Wait Until Element Is Visible    ${SEARCH_BOX}
    Element Should Be Visible        ${SEARCH_BOX}
    Element Should Be Enabled        ${SEARCH_BOX}

input search
    [Arguments]    ${product}
    # Step 2: Enter Product Name
    Clear Element Text               ${SEARCH_BOX}
    Input Text                       ${SEARCH_BOX}    ${product}

    # Assertion 2: Product Name Entered Correctly
    Textfield Value Should Be        ${SEARCH_BOX}    ${product}

input enter
    # Step 3: Press Enter
    Press Keys                       ${SEARCH_BOX}    ENTER
    Sleep    3s
validation
    # Assertion 3: Search Results Page Loaded
    Wait Until Page Contains         Search
#    Location Should Contain          route=product


    # Assertion 4: At Least One Product Result Appears
    Page Should Contain Element      ${FIRST_PRODUCT}


    # Assertion 5: Search Keyword Appears Somewhere
    Page Should Contain              ${PRODUCT_NAME}

    Log To Console    Product Search Completed Successfully!
