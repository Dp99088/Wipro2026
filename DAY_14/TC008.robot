*** Test cases ***
Print Names using for loop
    FOR     ${name}     IN     Ram Ravi Tej
        log to console      ${name}
    END

Print Names using while loop
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=       Evaluate    ${count} + 1
    END

IF Condition
    ${age}=     Set Variable    20
    IF  ${age} >= 18
        Log     Eligible to vote
    END

IF ELSE Example
    ${num}=     Set Variable    5
    IF  ${num} > 10
        Log     Greater than 10
    ELSE
        Log     Less than or equal to 10
    END

IF ELSE IF Example
    ${marks}=       Set Variable    75
    IF  ${marks} >= 90
        Log     Grade A
    ELSE IF ${marks} >= 75
        Log     Grade B
    ELSE
        Log     Grade C
    END

Inline IF Example
    ${status}=    Set Variable    PASS
    # Syntax: IF  condition  Keyword  Arguments
    IF    '${status}' == 'PASS'    Log To Console    Test Passed Successfully


BREAK Example
    FOR     ${i}    IN  RANGE       1   10
        IF  '${i} == 5'
            BREAK
        END
        Log     ${i}
    END

CONTINUE Example
    FOR     ${i}    IN  RANGE       1   6
        IF  '${i} == 3'
            CONTINUE
        END
        Log     ${i}
        END



WHILE Loop With BREAK
    ${i}=       Set Variable        1
    WHILE   True
        IF  '${i} == 4'
            BREAK
        END
        Log     ${i}
        ${i}=   Evaluate    ${i} + 1
    END


Try Except Example
    TRY
        FAIL    Something went wrong
    EXCEPT
        Log     Error handled
    FINALLY
        Log     Always executed
    END


Run Keyword if Example
    ${status}=      Set Variable        PASS
    Run Keyword if  '${status}' == 'PASS'   Log     Test Passed


Run Keyword Unless Example
    ${status}=      Set Variable        Fail
    Run Keyword Unless  '${status}' == 'PASS'   Log     Test Failed