*** Settings ***
Library    ../src/main_page_test_case.py

*** Keywords ***
Initialize Environment
    [Documentation]      각 Test Case 수행 시 환경 초기화를 위함
    No Operation

Close Environment
    [Documentation]      각 Test Case 완료 후 환경 정리를 위함
    No Operation

Access To Web Page
    [Arguments]    ${url}
    Check Main Page    ${url}

Access to Weather
    [Arguments]    ${url}
    Check Weather    ${url}

Access to News
    [Arguments]    ${url}
    Check News    ${url}

Check the Fail
    [Arguments]    ${url}
    Check Fail    ${url}
