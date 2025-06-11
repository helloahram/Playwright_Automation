*** Settings ***
Library    ../src/pages/bdd_pages.py

*** Keywords ***
웹 페이지 "${url}" 에 접속한다
    go_to    ${url}

페이지 타이틀을 확인한다
    check_page_title

타이틀은 "${title}" 이어야 한다
    title_should_be    ${title}
