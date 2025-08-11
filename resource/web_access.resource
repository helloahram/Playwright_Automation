*** Settings ***
Library    ../keywords/login_keywords.py
Library    ../keywords/mail_keywords.py
Library    ../src/main_page_test_case.py

*** Keywords ***
Initialize Environment
    [Documentation]      각 Test Case 수행 시 환경 초기화를 위함
    No Operation

Close Environment
    [Documentation]      각 Test Case 완료 후 환경 정리를 위함
    No Operation

Access To Web Page
    [Documentation]      Web Page 접속 확인 
    [Arguments]    ${url}
    Check Main Page    ${url}

Check the Web Title
    [Documentation]      Web Page Title 확인 
    [Arguments]    ${url}
    Check Web Title    ${url}

Access to Mail w Login
    [Documentation]      로그인 한 상태로 메일 화면 진입 
    [Arguments]    ${url}
    Access Mail w Login   ${url}

Access to Cafe
    [Documentation]      카페 화면 진입 
    [Arguments]    ${url}
    Access Cafe    ${url}

Access to News
    [Documentation]      뉴스 화면 진입 
    [Arguments]    ${url}
    Access News    ${url}

Access to Weather
    [Documentation]      날씨 화면 진입 
    [Arguments]    ${url}
    Access Weather    ${url}