## 🚀 설치 방법

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate      # Windows
```
### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. Playwright 브라우저 설치
```bash
playwright install
```

## 🧪 실행 방법

### 1. Robot Framework 테스트 실행
```bash
# robot 디렉토리 안에 있는 테스트 실행
robot robot/web_access.robot
```

### 2. Python 기반 Playwright 테스트 실행
```bash
pytest src/main_page_test_case.py -s
```

### 3. 전체 테스트 및 Slack 알림 전송 
```bash
./run_robot_and_noti.sh
```