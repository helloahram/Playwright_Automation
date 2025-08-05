import asyncio
from playwright.async_api import async_playwright


async def check_main_page(url: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await page.goto(url)
            print(await page.title())
        finally:
            await browser.close()


async def check_web_title(url: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await page.goto(url)
            assert await page.title() == "NAVER"
        finally:
            await browser.close()


async def access_weather(url: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await page.goto(url)
            await page.get_by_role("button", name="바로가기 펼침").click()
            async with page.expect_popup() as popup_info:
                await page.get_by_label("주요 서비스").get_by_role(
                    "link", name="날씨"
                ).click()
            page1 = await popup_info.value
            assert "날씨" in await page1.title()
        finally:
            await browser.close()


async def access_news(url: str):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await page.goto(url)
            await page.get_by_role("button", name="바로가기 펼침").click()
            async with page.expect_popup() as popup_info:
                await page.get_by_label("주요 서비스").get_by_role(
                    "link", name="뉴스"
                ).click()
            page1 = await popup_info.value
            assert "뉴스" in await page1.title()
        finally:
            await browser.close()


# 로컬에서 단독 실행할 때만 호출
if __name__ == "__main__":
    asyncio.run(check_main_page("https://www.naver.com"))
    asyncio.run(check_web_title("https://www.naver.com"))
    asyncio.run(check_weather("https://www.naver.com"))
    asyncio.run(check_news("https://www.naver.com"))
