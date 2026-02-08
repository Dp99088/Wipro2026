*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Browser    http://localhost:5000    edge    executable_path=C:/Users/prasa/PyCharmMiscProject/msedgedriver.exe
Suite Teardown    Close Browser



*** Test Cases ***
Register Patient
    Input Text    name=name    Durga Prasad
    Input Text    name=age     23
    Input Text
    Input Text    name=disease    Fever
    Input Text    name=doctor     Dr.Smith
    Click Button    Register

Register Multiple Patients
    [Template]    Register Patient Template
    Vijay    22
    Ajay      20

*** Keywords ***
Register Patient Template
    [Arguments]    ${name}    ${age}
    Input Text    name=name    ${name}
    Input Text    name=age     ${age}
    Click Button    Register
