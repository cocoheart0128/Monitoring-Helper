# 📊 AWS Glue Workflow Monitoring Dashboard

AWS Glue 워크플로우 실행 이력을 시각적으로 모니터링할 수 있는 Streamlit 기반 대시보드입니다.  
실패 Job 확인, 실행 소요 시간 분석, 성공률 파악 등 운영 효율성을 높일 수 있습니다.

---
## 🖥️ 주요 기능

🔎 지정된 AWS Glue Workflow 실행 내역 조회
✅ Job 단위 상태/로그/시간 시각화
📊 성공/실패 비율 표시
🔄 실시간 조회 (실제 AWS 계정 연동 시 가능)
📁 로컬 JSON 샘플 데이터 테스트 가능

---
## 🗂️ 예시 화면

<img width="1100" alt="截屏2025-06-26 下午10 01 50" src="https://github.com/user-attachments/assets/cfa0026b-1297-4a88-850a-2bd440a82850" />
<img width="1100" alt="截屏2025-06-26 下午10 01 01" src="https://github.com/user-attachments/assets/db225fe5-245f-40bc-9c05-90038a9461fe" />

---

## 🗂️ 프로젝트 구조

```plaintext
aws-glue-monitoring-app/
├── app/
│   └── app.py                   # Streamlit 대시보드 메인 파일
├── configs/
│   ├── workflow_config.json     # AWS 인증 정보 및 워크플로우 이름 설정
│   └── workflow_sample.json     # 테스트용 샘플 데이터
├── requirements.txt             # Python 패키지 의존성 목록
├── Dockerfile                   # Docker 이미지 정의 파일
├── deploy.yml                   # GitHub Actions 배포 설정
├── start.sh                     # 로컬 실행 스크립트
└── README.md                    # 문서 파일 (현재 파일)
```
---

🗂️ 프로젝트 구조2

```plaintext
aws-glue-monitoring-app/
├── app/
│   └── app.py                   # Streamlit 대시보드 메인 파일
├── configs/
│   ├── workflow_config.json     # AWS 인증 정보 및 워크플로우 이름 설정
│   └── workflow_sample.json     # 테스트용 샘플 데이터
├── requirements.txt             # Python 패키지 의존성 목록
├── Dockerfile                   # Docker 이미지 정의 파일
├── deploy.yml                   # GitHub Actions 배포 설정
├── start.sh                     # 로컬 실행 스크립트
└── README.md  
