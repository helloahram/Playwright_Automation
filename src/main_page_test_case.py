import time
from pages import page_v1
from playwright.sync_api import sync_playwright

def check_main_page(url:str):
    try:
        with sync_playwright() as playwright:
            page = page_v1(playwright)
            page.open(url)

            time.sleep(10)
            # install 4 carrier to ports
            page.close()

    finally:        
        pass
        # 해당 method 종료 시 무조건 실행하는 기능