import streamlit as st
import pandas as pd
# import boto3
import streamlit as st
from datetime import datetime
from collections import defaultdict
import json
import os

# acc_id = os.environ.get("AWS_ACCESS_KEY_ID")
# acc_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
###config format {"acc_id": "","acc_key": "","workflow_names": ["wf1","wf2"]}

config_path = os.path.join(os.path.dirname(__file__), "workflow_config.json")
print(config_path)
with open(config_path, "r") as f:
    config = json.load(f)

acc_id = config.get("acc_id", "")
acc_key = config.get("acc_key", "")
workflow_names = config.get("workflow_names", [])


###샘플 데이터 테스트용
workflow_names=["workflow_alpha","workflow_belta"]
sample_path = os.path.join(os.path.dirname(__file__), "workflow_sample.json")
with open(sample_path, "r") as f:
    workflow_sample = json.load(f)['workflow_sample']
def convert_jobruns_datetime(workflow_sample):
    for wf in workflow_sample:
        for run in wf.get('wf_runs', []):
            try:
                run["StartedOn"] = datetime.strptime(run["StartedOn"], "%Y-%m-%d %H:%M:%S")
                run["CompletedOn"] = datetime.strptime(run["CompletedOn"], "%Y-%m-%d %H:%M:%S")
            except Exception:
                run["StartedOn"] = datetime.strptime(run["StartedOn"], "%Y-%m-%d%H:%M:%S")
                run["CompletedOn"] = datetime.strptime(run["CompletedOn"], "%Y-%m-%d%H:%M:%S")
                
            graph = run.get('Graph', {})
            nodes = graph.get('Nodes', [])
            for node in nodes:
                job_details = node.get('JobDetails', {})
                job_runs = job_details.get('JobRuns', [])
                for jr in job_runs:
                    if 'StartedOn' in jr and isinstance(jr['StartedOn'], str):
                        try:
                            jr['StartedOn'] = datetime.strptime(jr['StartedOn'][:19], '%Y-%m-%dT%H:%M:%S')
                        except Exception:
                            jr['StartedOn'] = datetime.strptime(jr['StartedOn'][:19], '%Y-%m-%d%H:%M:%S')
                    if 'CompletedOn' in jr and isinstance(jr['CompletedOn'], str):
                        try:
                            jr['CompletedOn'] = datetime.strptime(jr['CompletedOn'][:19], '%Y-%m-%dT%H:%M:%S')
                        except Exception:
                            jr['CompletedOn'] = datetime.strptime(jr['CompletedOn'][:19], '%Y-%m-%d%H:%M:%S')
    return workflow_sample
workflow_sample = convert_jobruns_datetime(workflow_sample)


STATUS_ICONS = {'Success': '✅','Failed': '❌','Running': '🔄','Pending': '⏳','SUCCEEDED': '✅','FAILED': '❌','SKIPPED': '⚪','RUNNING': '🔄','PENDING': '⏳'}
STATUS_COLORS = {'Success': 'green','Failed': 'red','Running': 'orange','Pending': 'grey','SUCCEEDED': 'green','FAILED': 'red','SKIPPED': 'grey','RUNNING': 'orange',
                 'PENDING': 'grey'}

# AWS Glue client
# glue = boto3.client("glue",aws_access_key_id = acc_id,aws_secret_access_key = acc_key,verify=False)

# 실행 결과 상세 파싱 함수
def get_wf_runs_results(wf_run): 
    if wf_run['Status'] == 'RUNNING':
        wf_run_e_time, wf_run_status, wf_run_t_time = 'WF is still running', 'Running', ''
    else:
        wf_run_status = 'Success' if wf_run['Statistics']['SucceededActions'] == wf_run['Statistics']['TotalActions'] else 'Fail'
        wf_run_t_time = str(wf_run['CompletedOn'] - wf_run['StartedOn']).split('.')[0]
        wf_run_e_time = wf_run['CompletedOn'].strftime('%Y-%m-%d %H:%M:%S')

    # Job 정보 추출
    result = []
    nodes = wf_run['Graph']['Nodes']
    for node in nodes:
        if node['Type'] == 'JOB':
            if node.get('JobDetails') and node['JobDetails'].get('JobRuns'):
                job_run = node['JobDetails']['JobRuns'][0]
                job_state = job_run.get('JobRunState', 'UNKNOWN')
                job_log = job_run.get('ErrorMessage', '아마 성공?') if job_state == 'FAILED' else '아마 성공?'
                job_s_time = job_run.get('StartedOn','UNKNOWN')
                job_e_time = job_run.get('CompletedOn','UNKNOWN')
                job_t_time = job_e_time - job_s_time if job_s_time!='UNKNOWN' and job_e_time!='UNKNOWN' else 'UNKNOWN'
            else:
                job_state = 'NotRun'
                job_log = 'Empty'
                job_s_time = 'UNKNOWN'
                job_e_time = 'UNKNOWN'
                job_t_time = 'UNKNOWN'


            result_dict = {
                'job_name': node['Name'],
                'job_state': job_state,
                'job_log': job_log,
                's_time':job_s_time,
                'e_time':job_e_time,
                't_time': job_t_time
            }
            result.append(result_dict)

    return {
        'wf_name': wf_run['Name'],
        's_time': wf_run['StartedOn'].strftime('%Y-%m-%d %H:%M:%S'),
        'e_time': wf_run_e_time,
        't_time': wf_run_t_time,
        'status': wf_run_status,
        'detail': wf_run['Statistics'],
        'jobs': result,
        'wf_run_id': wf_run['WorkflowRunId']
    }


st.set_page_config(layout="wide")
st.title("AWS Workflow Monitoring Dashboard")

st.sidebar.title("⚙️ Workflow Settings")
# 공지사항 박스
st.sidebar.info("""
📢 **공지사항**

- 워크플로우 리스트는 **내장된 Config 파일**을 통해 불러옵니다.
- Config 파일 포맷은 아래와 같습니다:

```json
{
  "acc_id": "",
  "acc_key": "",
  "workflow_names": ["wf1", "wf2"]
}
""")

with st.sidebar.form("workflow_form"):
    max_results = st.number_input("Max Workflow Runs to Fetch", min_value=1, max_value=10, value=1)
    #uploaded_file = st.file_uploader("워크플로우 관련 파일 업로드", type=['csv', 'json', 'xlsx'])
    submitted = st.form_submit_button("🚀 Fetch Workflow Runs")

st.markdown("---")

if submitted:
    for workflow_name in workflow_names:
    # for i, workflow_name in enumerate(workflow_names, start=1):
        # renamed_wf_name = f"workflow{i}"
        st.header(f"🗂️ Workflow Name: {workflow_name}")  # 섹션 제목

        workflow_runs = []
        # wf_runs = glue.get_workflow_runs(Name=workflow_name, IncludeGraph=True, MaxResults=max_results)['Runs']
        wf_runs = next((wf for wf in workflow_sample if wf["wf_name"] == workflow_name),None)['wf_runs'][0:max_results]
        
        for wf_run in wf_runs:
            result = get_wf_runs_results(wf_run)

            # result['wf_name'] = renamed_wf_name
            # for j, job in enumerate(result['jobs'], start=1):
            #     job['job_name'] = f"{renamed_wf_name}_job{j}"

            workflow_runs.append(result)
        
        # 워크플로우 실행 목록을 순회하며 Expander 생성
        for run in workflow_runs:
            run_id = run['wf_name']
            status_icon = STATUS_ICONS.get(run['status'], '❓')
            status_color = STATUS_COLORS.get(run['status'], 'black')
        
            # 성공/전체 Job 수 계산
            successful_jobs = sum(1 for job in run['jobs'] if job['job_state'] == 'SUCCEEDED')
            total_jobs = len(run['jobs'])
            success_ratio = f"{successful_jobs} / {total_jobs}"


            # Expander 헤더 (워크플로우 요약 정보)
            expander_title = (
                f"{status_icon} run_date: {(run['s_time'])[0:10]}-------------------- Status:{run['status']}--------------------Success/Total: {success_ratio}"
            )

            with st.expander(expander_title, expanded=False):
                st.markdown(f"**Detail Job Execution Records for Workflow Name: `{run_id}`**")
        
                # Job 상세 정보를 담을 DataFrame 생성
                job_data = []
                for job in run['jobs']:
                    job_status_icon = STATUS_ICONS.get(job['job_state'], '❓')
                    job_status_color = STATUS_COLORS.get(job['job_state'], 'black')
                    job_name_display = f"<span style='color:{job_status_color};'>↳ {job['job_name']}</span>"
        
                    job_data.append({
                        'Run ID / Job': job_name_display,
                        'Start Time': job.get('s_time', 'N/A'),
                        'End Time': job.get('e_time', 'N/A'),
                        'Duration': job.get('t_time', 'N/A'),
                        'Status': f"<span style='color:{job_status_color};'>{job_status_icon}</span>",
                    })
                
                df_jobs = pd.DataFrame(job_data)
                
                # HTML을 렌더링하기 위해 escape=False 사용
                st.markdown(df_jobs.to_html(escape=False, index=False), unsafe_allow_html=True)

    st.markdown("---")
    st.info("Click on a workflow run to view its detailed job execution records.")
else: 
    st.info("📋 설정을 완료한 후 'Fetch Workflow Runs' 버튼을 눌러주세요.")
