*** Settings ***
Library    RequestsLibrary


*** Variables ***
${baseurl}  http://127.0.0.1:5000

*** Test Cases ***
Verify Get All User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Verify Get Single User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/2
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

Create new user
    ${data}=    create dictionary    name=hema
    Create Session    mysession    ${baseurl}

    ${response}=    POST On Session    mysession    /users    json=${data}
    Status Should Be    201    ${response}

    ${res_json}=    Set Variable    ${response.json()}
    Log    ${res_json}    console=True

update user
        Create session      mysession       ${baseurl}
        ${data}=    create dictionary       name=pooja
        ${response}=        PUT on session      mysession       /users/1        json=${data}
        status should be    200     ${response}
        ${res_json}=    Set Variable    ${response.json()}
        Log    ${res_json}    console=True


patch user
        Create session      mysession       ${baseurl}
        ${data}=    create dictionary       name=pooja patched
        ${response}=        PATCH on session      mysession       /users/1        json=${data}
        status should be    200     ${response}
        ${res_json}=    Set Variable    ${response.json()}
        Log    ${res_json}    console=True


Verify Delete user by userid
        Create Session    mysession             ${baseurl}
        ${response}=  DELETE On Session    mysession   /users/1
        Status Should Be    200     ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True





