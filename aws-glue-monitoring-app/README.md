# 📊 AWS Glue Workflow Monitoring Dashboard

AWS Glue 워크플로우 실행 이력을 시각적으로 모니터링할 수 있는 Streamlit 기반 대시보드입니다.  
실패 Job 확인, 실행 소요 시간 분석, 성공률 파악 등 운영 효율성을 높일 수 있습니다.

---
## 🖥️ 주요 기능

- 🔎 **지정된 AWS Glue Workflow 실행 내역 조회**
- ✅ **Job 단위 상태/로그/시간 시각화**
- 📊 **성공/실패 비율 표시**
- 🔄 **실시간 조회** (실제 AWS 계정 연동 시 가능)
- 📁 **로컬 JSON 샘플 데이터 테스트 가능**

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

## 🚀 실행 방법

1. 로컬에서 실행
```
pip install -r requirements.txt
streamlit run app.py
``` 
2. Docker로 실행
```
docker build -t aws-glue-monitoring-app .
docker run -p 8501:8501 aws-glue-monitoring-app
```

## 📌 사용 방법

1. Config 파일 설정

    workflow_config.json 파일에 모니터링할 워크플로우 이름과 AWS 인증 정보 입력
    또는 .env 파일 사용 시 내부 코드를 해당 환경변수로 수정 가능

2. 사이드바에서 설정

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="width: 30%; vertical-align: top; padding: 0;">
      <img src="https://github.com/user-attachments/assets/dd21545c-0ccf-4090-8846-cb49d96683ce" alt="사이드바 설정" style="width: 100%; max-width: 100%;" />
    </td>
    <td style="width: 70%; vertical-align: top; padding: 0 0 0 10px;">
      <p><strong>좌측 사이드바에서 다음 설정을 진행합니다:</strong></p>
      <ul>
        <li><strong>Max Workflow Runs to Fetch</strong><br />불러올 실행 이력 수 설정 (1~10)</li>
        <li><strong>Fetch Workflow Runs 버튼 클릭</strong><br />설정된 워크플로우 이름에 대해 실행 이력을 불러옵니다.</li>
      </ul>
    </td>
  </tr>
</table>

3. 대시보드 확인

    워크플로우별 실행 이력을 다음과 같이 확인할 수 있습니다:
    
    - 🔽 날짜별 실행 내역이 Expander로 나열됨
    
    - ✅ 각 실행 내에서 JOB 별 실행 상태, 시간, 소요 시간, 실패 여부를 확인 가능
    
    - ✔️ 상태에 따라 ✅(성공), ❌(실패), ⏳(대기), 🔄(실행 중) 아이콘 표시
    
    - 📈 성공/전체 Job 비율로 워크플로우 성공률 시각화


## ▶️ 예시 화면


<img width="1100" alt="截屏2025-06-26 下午10 01 50" src="https://github.com/user-attachments/assets/cfa0026b-1297-4a88-850a-2bd440a82850" />
<img width="1100" alt="截屏2025-06-26 下午10 01 01" src="https://github.com/user-attachments/assets/db225fe5-245f-40bc-9c05-90038a9461fe" />


## ⚠️ 주의사항

workflow_config.json에 AWS 자격 증명을 직접 포함하지 말고,
.env 또는 GitHub Secrets를 통한 보안 처리 권장

샘플 데이터를 사용하는 경우 실제 AWS 호출은 일어나지 않음

Production 배포 시 SSL 인증 적용, 사용자 인증 추가 고려 필요
