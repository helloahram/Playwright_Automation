import time
from pages.pages import page_v1
from playwright.sync_api import sync_playwright


def check_main_page(url: str):
    try:
        with sync_playwright() as playwright:
            page = page_v1(playwright)
            page.open(url)

            time.sleep(5)
            # install 4 carrier to ports
            page.close()

    finally:
        pass
        # 해당 method 종료 시 무조건 실행하는 기능


def check_web_title(url: str):
    try:
        with sync_playwright() as playwright:
            page = page_v1(playwright)
            page.open(url)

            assert page.title() == "NAVER"
            page.close()

    finally:
        pass


def check_weather(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            page.get_by_role("button", name="바로가기 펼침").click()
            with page.expect_popup() as page1_info:
                page.get_by_label("주요 서비스").get_by_role(
                    "link", name="날씨"
                ).click()
            page1 = page1_info.value

            # 검증: 페이지 타이틀에 "날씨" 포함
            assert "날씨" in page1.title()

        finally:
            browser.close()


def check_news(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            page.get_by_role("button", name="바로가기 펼침").click()
            with page.expect_popup() as page1_info:
                page.get_by_label("주요 서비스").get_by_role(
                    "link", name="뉴스"
                ).click()
            page1 = page1_info.value

            # 검증: 페이지 타이틀에 "뉴스" 포함
            assert "뉴스" in page1.title()

        finally:
            browser.close()


def check_fail(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            page.get_by_role("button", name="바로가기 펼침").click()
            with page.expect_popup() as page1_info:
                page.get_by_label("주요 서비스").get_by_role(
                    "link", name="뉴스"
                ).click()
            page1 = page1_info.value

            # 의도된 Fail
            assert "날씨" in page1.title()

        finally:
            browser.close()
