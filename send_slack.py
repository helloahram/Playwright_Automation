import xml.etree.ElementTree as ET
import requests


# 테스트 결과 파싱 함수
def parse_robot_output(xml_path):
    tree = ET.parse(xml_path)  # XML 파일을 파싱해서 트리 객체 생성
    root = tree.getroot()  # 루트 엘리먼트 (<robot>) 가져오기

    total_tests = 0
    passed = 0
    failed = 0
    failed_tests = []

    for test in root.iter("test"):  # 모든 테스트 케이스 순회
        total_tests += 1
        name = test.attrib.get("name", "Unknown Test")  # 테스트 이름 가져오기
        status_elem = test.find("status")  # <status> 엘리먼트 찾기
        if status_elem is not None:
            status = status_elem.attrib.get("status")  # status="PASS"/"FAIL"
            if status == "PASS":
                passed += 1
            else:
                failed += 1
                failed_tests.append(name)

    return total_tests, passed, failed, failed_tests


# Slack으로 전송하는 함수
def send_to_slack(message, webhook_url):
    response = requests.post(webhook_url, json={"text": message})
    print(f"Slack 응답: {response.status_code}, {response.text}")


# 메인 실행
if __name__ == "__main__":
    xml_path = "output.xml"
    webhook_url = "https://hooks.slack.com/services/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"

    total, passed, failed, failed_tests = parse_robot_output(xml_path)

    emoji = "✅" if failed == 0 else "❌"
    message = f"""{emoji} *Robot Framework 테스트 결과*
총 테스트: {total}
✅ 성공: {passed}
❌ 실패: {failed}"""

    if failed_tests:
        failed_list = "\n• " + "\n• ".join(failed_tests)
        message += f"\n\n*실패한 테스트 목록:*\n{failed_list}"

    send_to_slack(message, webhook_url)

print(f"📦 파싱된 결과: 총 {total}, 성공 {passed}, 실패 {failed}")
print("📨 Slack으로 보낼 메시지:")
print(message)
