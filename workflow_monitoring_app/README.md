# 📊 AWS Glue Workflow Monitoring Dashboard

Streamlit 기반의 AWS Glue Workflow 실행 모니터링 대시보드입니다.  
워크플로우 실행 이력과 각 Job 상태를 시각화하여 파이프라인 운영 상태를 빠르게 파악할 수 있습니다.

---

## 🗂️ 프로젝트 구조

```bash
aws-glue-monitoring-app/
├── app/
│   └── app.py                   # Streamlit 대시보드 메인 파일
├── configs/
│   ├── workflow_config.json     # AWS 인증 및 모니터링 대상 워크플로우 설정
│   └── workflow_sample.json     # 테스트용 샘플 워크플로우 데이터
├── requirements.txt             # Python 의존성 목록
├── Dockerfile                   # Docker 이미지 빌드 설정
├── deploy.yml                   # GitHub Actions 또는 수동 배포용 설정 파일
├── start.sh                     # 로컬 실행 스크립트
└── README.md                    # 사용 설명서


⚙️ 설정
🔧 configs/workflow_config.json
json
복사
편집
{
  "acc_id": "YOUR_AWS_ACCESS_KEY_ID",
  "acc_key": "YOUR_AWS_SECRET_ACCESS_KEY",
  "workflow_names": ["workflow_alpha", "workflow_belta"]
}
acc_id, acc_key: AWS Glue에 접근할 수 있는 자격 증명

workflow_names: 모니터링할 Glue Workflow 이름 리스트

✅ 운영 환경에서는 이 파일 대신 .env 또는 AWS Secrets Manager 사용을 권장합니다.

🧪 configs/workflow_sample.json
샘플 데이터 기반으로 UI를 테스트할 수 있습니다 (AWS 미연결 환경에서 사용 가능).

json
복사
편집
{
  "workflow_sample": [
    {
      "wf_name": "workflow_alpha",
      "wf_runs": [
        {
          "Name": "workflow_alpha",
          "WorkflowRunId": "alpha-run-001",
          "StartedOn": "2025-06-26 08:00:00",
          "CompletedOn": "2025-06-26 08:20:00",
          "Status": "SUCCEEDED",
          "Statistics": {
            "TotalActions": 5,
            "SucceededActions": 5,
            "FailedActions": 0
          },
          "Graph": {
            "Nodes": [
              {
                "Type": "JOB",
                "Name": "alpha_job_1",
                "UniqueId": "123456",
                "JobDetails": {
                  "JobRuns": [
                    {
                      "JobRunState": "SUCCEEDED",
                      "StartedOn": "2025-06-26T08:00:00",
                      "CompletedOn": "2025-06-26T08:10:00"
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
🧪 로컬 실행 방법
1. 패키지 설치
bash
복사
편집
pip install -r requirements.txt
2. 실행 스크립트로 실행
bash
복사
편집
./start.sh
✅ start.sh
bash
복사
편집
#!/bin/bash
echo "🚀 Running Glue Monitor..."
streamlit run app/app.py
🐳 Docker로 실행하기
이미지 빌드
bash
복사
편집
docker build -t glue-monitor .
컨테이너 실행
bash
복사
편집
docker run -p 8501:8501 glue-monitor
🐳 Dockerfile
dockerfile
복사
편집
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
🚀 배포 자동화 (GitHub Actions)
deploy.yml 예시
yaml
복사
편집
name: Deploy to Server

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout source
      uses: actions/checkout@v3

    - name: SSH and deploy
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_IP }}
        username: ${{ secrets.SERVER_USER }}
        key: ${{ secrets.SSH_PRIVATE_KEY }}
        script: |
          cd /your/app/path
          git pull origin main
          docker build -t glue-monitor .
          docker stop glue-monitor || true && docker rm glue-monitor || true
          docker run -d -p 8501:8501 --name glue-monitor glue-monitor
GitHub Secrets
Key	설명
SERVER_IP	EC2 또는 배포 서버 IP 주소
SERVER_USER	SSH 로그인 사용자 이름
SSH_PRIVATE_KEY	GitHub에서 사용할 개인 SSH 키 전체

🖥️ 사용 방법
workflow_config.json에서 AWS 인증 정보 및 Workflow 목록 설정

start.sh 또는 Docker로 앱 실행

좌측 사이드바에서 조회할 실행 수 설정 후 "🚀 Fetch Workflow Runs" 클릭

각 워크플로우 실행 내역과 Job 상태, 시작/종료 시간, 로그 확인 가능

📊 UI 미리보기
🗂️ 모니터링 메인 화면

🔍 상세 실행 결과

🎨 상태 아이콘 안내
상태	아이콘	색상
SUCCEEDED	✅	Green
FAILED	❌	Red
RUNNING	🔄	Orange
SKIPPED	⚪	Gray
PENDING	⏳	Gray

🛡️ 보안 권장 사항
workflow_config.json에 자격 증명을 직접 저장하지 마세요.

.env, AWS Systems Manager, GitHub Secrets 등을 활용하여 민감 정보 보호

외부 공개 환경에서는 인증/암호 설정 및 HTTPS 적용 권장

💡 향후 개선 아이디어
Slack/Email 알림 연동

실패 Job 자동 감지 및 재시도 로직 제안

Glue Step Functions, Airflow 연동

히스토리 DB 저장 및 차트 분석 기능 추가

사용자 인증 기능 (ex. Streamlit Authenticator)

📄 라이선스
MIT License

🙌 기여
PR 및 Issue 언제든지 환영합니다!
함께 더 나은 운영 도구를 만들어봐요 :)

yaml
복사
편집
