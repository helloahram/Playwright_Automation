# keywords/mail_keywords.py
from login_keywords import load_logged_in_context


def open_mail_page():
    async def run():
        browser, context = await load_logged_in_context()
        page = await context.new_page()
        await page.goto("https://www.naver.com")

        await page.get_by_role("link", name="메일").click()
        await page.wait_for_url("https://mail.naver.com/*")

        assert "메일" in await page.title()
        await browser.close()

    return run()
