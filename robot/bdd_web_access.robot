*** Settings ***
Resource    ../resource/bdd_web_access.resource

*** Variables ***
${NAVER_URL}      https://www.naver.com
${EXPECTED_TITLE}     NAVER

*** Test Cases ***
Scenario: NAVER 메인 페이지 접속 시 정상적으로 열려야 한다
    Given 웹 페이지 "${NAVER_URL}" 에 접속한다
    When 페이지 타이틀을 확인한다
    Then 타이틀은 "${EXPECTED_TITLE}" 이어야 한다