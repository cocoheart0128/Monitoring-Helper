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
