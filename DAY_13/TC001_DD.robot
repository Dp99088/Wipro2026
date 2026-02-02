*** Settings ***

Library    SeleniumLibrary
*** Variables ***
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      chrome
${username}     Admin
${password}     admin123

*** Keywords ***
open orangehrm
    Open Browser    ${url}   chrome
    Maximize Browser Window
orangehrmlogin
    [Arguments]    ${username}   ${password}
    Sleep    5s
    Input Text    name=username    ${username}
    Sleep    5s
    Input Text    name=password    ${password}
    sleep        5s
    Capture Page Screenshot    beforelogin.png
    Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Sleep    5s
    Capture Page Screenshot    afterlogin.png
    Close Browser

*** Test Cases ***
TC001_DD.robot
    Open Orangehrm
    Orangehrmlogin    Admin   admin123

