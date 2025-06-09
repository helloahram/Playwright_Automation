from playwright.sync_api import Playwright, expect

class page_v1:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(viewport={"width": 2560, "height": 1310})
        self.page = self.context.new_page()
    
    def open(self,url:str):
        self.page.goto(url)

    def close(self):
        self.context.close()
        self.browser.close()