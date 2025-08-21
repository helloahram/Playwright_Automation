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

    import asyncio

    try:
        # 현재 스레드에 이벤트 루프가 없으면
        # 여기서 새 루프를 만들어 run()을 끝날 때까지 실행
        return asyncio.run(run())
    except RuntimeError:
        # 이미 이벤트 루프가 돌고 있는 환경이면
        # 여기서 실행하면 충돌하니 코루틴만 넘기고 호출자가 await 하게 함
        return run()
