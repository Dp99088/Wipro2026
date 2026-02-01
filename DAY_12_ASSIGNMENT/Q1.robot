*** Settings ***

Library           SeleniumLibrary

*** Variables ***

${Name}            Durga Prasad

${Course}        Robot Framework

@{Numbers}            5     6     7     8


*** Test Cases ***
Log Basic Information
    Log         Starting first test case
    Log To Console         Hello ${Name}
    Log To Console        Learning ${Course}
    Log        First test case completed
    Log         Starting second test case
    Log To Console     Marks are @{Numbers}
    Log         Second test case completed