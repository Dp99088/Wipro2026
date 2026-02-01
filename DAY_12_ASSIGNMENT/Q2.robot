*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary

*** Test Cases ***
Verify Python And Robot Framework Installation
    ${python}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Log To Console    Python Version: ${python.stdout}

    ${robot}=     Run Process    robot    --version    stdout=PIPE    stderr=PIPE
    Log To Console    Robot Framework Version: ${robot.stdout}

    Log To Console    SeleniumLibrary imported successfully