# script/save_login_session.py (핵심 부분만)
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PWTimeout

SESSION_PATH = Path(__file__).resolve().parents[1] / "naver_logged_in.json"
LOGIN_URL = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"


async def save_login_session():
    print(f"💾 세션 저장 경로: {SESSION_PATH}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # 1) 네이버 '로그인' 페이지로 바로 이동
        print("🔐 로그인 페이지로 이동...")
        await page.goto(LOGIN_URL, wait_until="domcontentloaded")

        # 2) 사용자 수동 로그인
        print("\n📝 수동 로그인 후 터미널에서 엔터를 누르세요")
        input("✅ 로그인 완료 후 엔터 ⏎ : ")

        # 3) 로그인 후 네트워크/리다이렉트 안정화 대기
        try:
            await page.wait_for_load_state("networkidle", timeout=5000)
        except PWTimeout:
            pass

        # 4) 세션 저장 (브라우저 닫으면 안 됨)
        await context.storage_state(path=str(SESSION_PATH))
        print(f"✅ 세션 저장 완료: {SESSION_PATH}")
        try:
            data = json.loads(SESSION_PATH.read_text(encoding="utf-8"))
            print(f"🍪 저장된 쿠키 수: {len(data.get('cookies', []))}")
            # 파일은 멀쩡하지만 로그인 정보가 안 들어있을 수 있음
            if len(data.get("cookies", [])) == 0:
                print("⚠️ 쿠키 없음 → 세션이 유효하지 않을 수 있음")
        # 파일이 깨졌거나, 쓰기 도중 손상, 혹은 JSON이 아닌 내용일 때
        except Exception:
            print("⚠️ JSON 파싱은 실패했지만, 파일은 생성됐습니다.")

        await browser.close()
        print("🔚 브라우저 닫힘")


if __name__ == "__main__":
    asyncio.run(save_login_session())
