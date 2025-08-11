# keywords/login_keywords.py
from playwright.async_api import async_playwright

SESSION_PATH = "naver_logged_in.json"


def load_logged_in_context():
    async def run():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(storage_state=SESSION_PATH)
            return browser, context

    return run()
