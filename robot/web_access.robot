*** Settings ***
Resource    ../resource/web_access.resource
Test Setup    Initialize Environment
Test Teardown    Close Environment

*** Test Cases ***
NAVER : Check Main Page
    Access To Web Page    https://www.naver.com