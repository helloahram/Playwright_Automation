from playwright.sync_api import sync_playwright


def check_main_page(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            print(page.title())
        finally:
            browser.close()


def check_web_title(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            assert page.title() == "NAVER"
        finally:
            browser.close()


def check_weather(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            page.get_by_role("button", name="바로가기 펼침").click()
            with page.expect_popup() as popup_info:
                page.get_by_label("주요 서비스").get_by_role(
                    "link", name="날씨"
                ).click()
            page1 = popup_info.value
            assert "날씨" in page1.title()
        finally:
            browser.close()


def check_news(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url)
            page.get_by_role("button", name="바로가기 펼침").click()
            with page.expect_popup() as popup_info:
                page.get_by_label("주요 서비스").get_by_role(
                    "link", name="뉴스"
                ).click()
            page1 = popup_info.value
            assert "뉴스" in page1.title()
        finally:
            browser.close()


if __name__ == "__main__":
    check_main_page("https://www.naver.com")
    check_web_title("https://www.naver.com")
    check_weather("https://www.naver.com")
    check_news("https://www.naver.com")
