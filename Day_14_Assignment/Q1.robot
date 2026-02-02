*** Settings ***
Documentation     A sample suite demonstrating Setup, Teardown, and Tags.
Suite Setup       Log To Console    \n--- Starting Entire Test Suite ---
Suite Teardown    Log To Console    \n--- Finishing Entire Test Suite ---
Test Setup        Log To Console    \n- Preparing for specific test case
Test Teardown     Log To Console    \n- Cleaning up after test case

*** Test Cases ***
Successful Login Scenario
    [Tags]    Sanity    Regression
    Log To Console    Executing the Login Test...
    Should Be Equal    1    1

Database Connection Test
    [Tags]    Database
    Log To Console    Executing the Database Test...
    No Operation