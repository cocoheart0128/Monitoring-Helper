# 📊 AWS Glue Workflow Monitoring Dashboard

AWS Glue 워크플로우 실행 이력을 시각적으로 모니터링할 수 있는 Streamlit 기반 대시보드입니다.  
실패 Job 확인, 실행 소요 시간 분석, 성공률 파악 등 운영 효율성을 높일 수 있습니다.

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

---

## 🗂️ 프로젝트 구조2

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
