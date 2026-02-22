*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    ../variables/e2e_flow_data.csv

Resource   ../keywords/register_keywords.robot
Resource    ../keywords/login_keywords.robot
Resource    ../resources/common.robot
Resource    ../keywords/cart_keywords.robot
Resource   ../keywords/search_keywords.robot
Resource    ../keywords/product_keywords.robot
Resource    ../keywords/cart_update_remove_keywords.robot



Suite Setup     Open Site
Suite Teardown  Close Site
Test Teardown   Capture Screenshot On Failure


Test Template   end to end flow


*** Test Cases ***

end to end test for user- ${firstname} ${lastname}

*** Keywords ***
end to end flow
    [Arguments]    ${firstname}    ${lastname}    ${phone}    ${password}    ${product}
    Register New User
    input firstname    ${firstname}
    input lastname    ${lastname}
    input email    
    Input Phone    ${phone}
    input password    ${password}
    Click agree
    Click continue
    Click logout
    Login User Successfully    ${password}
    Search Products
    input search    ${product}
    input enter
    validation
    Open First Product Details
    Add Product To Cart And Validate Success
    Update Cart Quantity And Remove Item
    Logout User Successfully
