*** Settings ***
Library    ../src/main_page_test_case.py

*** Keywords ***
Check the Web Title
    [Arguments]    ${url}
    Check Web Title     ${url}
