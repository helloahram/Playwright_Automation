*** Settings ***
Resource    ../resource/web_access.resource
Resource    ../resource/main_page.resource
Test Setup    Initialize Environment
Test Teardown    Close Environment

*** Test Cases ***
NAVER : Check Main Page
    Access To Web Page    https://www.naver.com
    Check Web Title   https://www.naver.com

NAVER : Check the Weather
    Check Weather   https://www.naver.com

NAVER : Check the News
    Check News   https://www.naver.com
