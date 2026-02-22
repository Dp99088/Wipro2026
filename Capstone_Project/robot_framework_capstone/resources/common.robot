*** Settings ***

Library    SeleniumLibrary
Library    Screenshot

Resource   ../variables/testdata.robot



*** Keywords ***

Open Site
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    10s


Close Site
    Close Browser


Capture Screenshot On Failure
    Run Keyword If Test Failed    Capture Page Screenshot
