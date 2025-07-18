from playwright.sync_api import Playwright, expect, sync_playwright

# 글로벌 상태 저장 변수
_browser = None
_page = None
_context = None
_title = ""


def go_to(url):
    global _browser, _page, _context
    pw = sync_playwright().start()
    _browser = pw.chromium.launch(headless=True)
    _context = _browser.new_context(viewport={"width": 2560, "height": 1310})
    _page = _context.new_page()
    _page.goto(url)


class page_v1:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context(
            viewport={"width": 2560, "height": 1310}
        )
        self.page = self.context.new_page()

    def open(self, url: str):
        self.page.goto(url)

    def title(self) -> str:
        return self.page.title()

    def search(self, keyword: str):
        self.page.fill('input[name="query"]', keyword)
        self.page.keyboard.press("Enter")

    def get_content(self) -> str:
        self.page.wait_for_selector("body", timeout=5000)
        return self.page.content()

    def validate_result_contain(self, keyword):
        self.page.wait_for_selector("body", timeout=5000)
        assert keyword in self.page.content()

    def close(self):
        self.context.close()
        self.browser.close()
