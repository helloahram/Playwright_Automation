from playwright.sync_api import sync_playwright

# 글로벌 상태 저장 변수
_browser = None
_page = None
_context = None
_title = ""

def go_to(url):
    global _browser, _page, _context
    pw = sync_playwright().start()
    _browser = pw.chromium.launch(headless=False)
    _context = _browser.new_context()
    _page = _context.new_page()
    _page.goto(url)

def check_page_title():
    global _title
    if not _page:
        raise Exception("페이지가 아직 열리지 않았습니다.")
    _title = _page.title()

def title_should_be(expected):
    global _title
    if _title != expected:
        raise AssertionError(f"타이틀 불일치. 예상: {expected}, 실제: {_title}")
    _close()

def _close():
    global _browser
    if _browser:
        _browser.close()
