*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Sleep       5s
    Maximize Browser Window

*** Test Cases ***
TC001.robot
    Open Application
    Title Should Be    Google
    capture page screenshot
    Close Browser