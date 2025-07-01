from datetime import datetime, timedelta
from dateutil.tz import tzlocal

def make_job_sample():
  sample_job_runs = {
      "job2": [
          {
              'Id': 'jr_b201',
              'Attempt': 0,
              'TriggerName': 'tg2',
              'JobName': 'job2',
              'StartedOn': datetime(2025, 7, 1, 10, 0, 0, 100000, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 10, 0, 30, 500000, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 10, 0, 30, 500000, tzinfo=tzlocal()),
              'JobRunState': 'FAILED',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 30,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
          {
              'Id': 'jr_b202',
              'Attempt': 0,
              'TriggerName': 'tg2',
              'JobName': 'job2',
              'StartedOn': datetime(2025, 7, 1, 9, 50, 0, 300000, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 9, 50, 20, 900000, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 9, 50, 20, 900000, tzinfo=tzlocal()),
              'JobRunState': 'SUCCEEDED',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 20,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
          {
              'Id': 'jr_b203',
              'Attempt': 0,
              'TriggerName': 'tg2',
              'JobName': 'job2',
              'StartedOn': datetime(2025, 7, 1, 9, 40, 0, 700000, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 9, 45, 0, 700000, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 9, 45, 0, 700000, tzinfo=tzlocal()),
              'JobRunState': 'TIMEOUT',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 300,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
      ],
      "job3": [
          {
              'Id': 'jr_c301',
              'Attempt': 0,
              'TriggerName': 'tg3',
              'JobName': 'job3',
              'StartedOn': datetime(2025, 7, 1, 10, 10, 0, 0, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 10, 10, 30, 0, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 10, 10, 30, 0, tzinfo=tzlocal()),
              'JobRunState': 'RUNNING',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 0,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
          {
              'Id': 'jr_c302',
              'Attempt': 0,
              'TriggerName': 'tg3',
              'JobName': 'job3',
              'StartedOn': datetime(2025, 7, 1, 9, 55, 0, 0, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 9, 55, 25, 0, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 9, 55, 25, 0, tzinfo=tzlocal()),
              'JobRunState': 'SUCCEEDED',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 25,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
          {
              'Id': 'jr_c303',
              'Attempt': 0,
              'TriggerName': 'tg3',
              'JobName': 'job3',
              'StartedOn': datetime(2025, 7, 1, 9, 50, 0, 0, tzinfo=tzlocal()),
              'LastModifiedOn': datetime(2025, 7, 1, 9, 50, 40, 0, tzinfo=tzlocal()),
              'CompletedOn': datetime(2025, 7, 1, 9, 50, 40, 0, tzinfo=tzlocal()),
              'JobRunState': 'FAILED',
              'Arguments': {},
              'PredecessorRuns': [],
              'AllocatedCapacity': 0,
              'ExecutionTime': 40,
              'Timeout': 2880,
              'MaxCapacity': 0.125,
              'LogGroupName': '/aws-glue/python-jobs',
              'GlueVersion': '3.0',
              'ExecutionClass': 'STANDARD',
          },
      ]
  }
  return sample_job_runs



def make_crawler_sample():
    sample_crawler_runs = {
        "crawler1": [
            {
                'CrawlerMetricsList': [
                    {
                        'CrawlerName': 'crawler1',
                        'TimeLeftSeconds': 0.0,
                        'StillEstimating': False,
                        'LastRuntimeSeconds': 69.688,
                        'MedianRuntimeSeconds': 60.034,
                        'TablesCreated': 5,
                        'TablesUpdated': 3,
                        'TablesDeleted': 0
                    }
                ],
                'ResponseMetadata': {
                    'RequestId': 'c527',
                    'HTTPStatusCode': 200,
                    'HTTPHeaders': {
                        'date': 'Tue, 01 Jul 2025 05:41:21 GMT',
                        'content-type': 'application/x-amz-json-1.1',
                        'content-length': '240',
                        'connection': 'keep-alive',
                        'x-amzn-requestid': 'c527',
                        'cache-control': 'no-cache'
                    },
                    'RetryAttempts': 0
                }
            },
            {
                'Name': 'crawler1',
                'Role': 'crawler-role',
                'Targets': {
                    'S3Targets': [
                        {'Path': 's3://bucket/folder/', 'Exclusions': []}
                    ],
                    'JdbcTargets': [],
                    'MongoDBTargets': [],
                    'DynamoDBTargets': [],
                    'CatalogTargets': [],
                    'DeltaTargets': [],
                    'IcebergTargets': [],
                    'HudiTargets': []
                },
                'DatabaseName': 'test',
                'Classifiers': [],
                'RecrawlPolicy': {'RecrawlBehavior': 'CRAWL_NEW_FOLDERS_ONLY'},
                'SchemaChangePolicy': {'UpdateBehavior': 'LOG', 'DeleteBehavior': 'LOG'},
                'LineageConfiguration': {'CrawlerLineageSettings': 'DISABLE'},
                'State': 'READY',
                'TablePrefix': 'crt_stock_',
                'CrawlElapsedTime': 0,
                'CreationTime': datetime(2023, 9, 25, 16, 57, 44, tzinfo=tzlocal()),
                'LastUpdated': datetime(2025, 6, 17, 8, 18, tzinfo=tzlocal()),
                'LastCrawl': {
                    'Status': 'SUCCEEDED',
                    'LogGroup': '/aws-glue/crawlers',
                    'LogStream': 'crawler1',
                    'MessagePrefix': '164a',
                    'StartTime': datetime(2025, 7, 1, 1, 52, 46, tzinfo=tzlocal())
                },
                'Version': 4,
                'Configuration': '{"Version":1.0,"CreatePartitionIndex":false}',
                'LakeFormationConfiguration': {'UseLakeFormationCredentials': False, 'AccountId': ''}
            }
        ],
        "crawler2": [
            {
                'CrawlerMetricsList': [
                    {
                        'CrawlerName': 'crawler2',
                        'TimeLeftSeconds': 0.0,
                        'StillEstimating': False,
                        'LastRuntimeSeconds': 105.22,
                        'MedianRuntimeSeconds': 98.43,
                        'TablesCreated': 8,
                        'TablesUpdated': 0,
                        'TablesDeleted': 1
                    }
                ],
                'ResponseMetadata': {
                    'RequestId': 'd913',
                    'HTTPStatusCode': 200,
                    'HTTPHeaders': {
                        'date': 'Tue, 01 Jul 2025 06:11:42 GMT',
                        'content-type': 'application/x-amz-json-1.1',
                        'content-length': '250',
                        'connection': 'keep-alive',
                        'x-amzn-requestid': 'd913',
                        'cache-control': 'no-cache'
                    },
                    'RetryAttempts': 0
                }
            },
            {
                'Name': 'crawler2',
                'Role': 'crawler-role',
                'Targets': {
                    'S3Targets': [
                        {'Path': 's3://another-bucket/data/', 'Exclusions': ['*.tmp']}
                    ],
                    'JdbcTargets': [],
                    'MongoDBTargets': [],
                    'DynamoDBTargets': [],
                    'CatalogTargets': [],
                    'DeltaTargets': [],
                    'IcebergTargets': [],
                    'HudiTargets': []
                },
                'DatabaseName': 'analytics',
                'Classifiers': [],
                'RecrawlPolicy': {'RecrawlBehavior': 'CRAWL_EVERYTHING'},
                'SchemaChangePolicy': {'UpdateBehavior': 'UPDATE_IN_DATABASE', 'DeleteBehavior': 'DELETE_FROM_DATABASE'},
                'LineageConfiguration': {'CrawlerLineageSettings': 'ENABLE'},
                'State': 'READY',
                'TablePrefix': 'etl_',
                'CrawlElapsedTime': 0,
                'CreationTime': datetime(2024, 1, 10, 10, 0, 0, tzinfo=tzlocal()),
                'LastUpdated': datetime(2025, 6, 30, 15, 0, tzinfo=tzlocal()),
                'LastCrawl': {
                    'Status': 'FAILED',
                    'LogGroup': '/aws-glue/crawlers',
                    'LogStream': 'crawler2',
                    'MessagePrefix': '2fbc',
                    'StartTime': datetime(2025, 7, 1, 2, 5, 30, tzinfo=tzlocal())
                },
                'Version': 7,
                'Configuration': '{"Version":1.0,"CreatePartitionIndex":true}',
                'LakeFormationConfiguration': {'UseLakeFormationCredentials': True, 'AccountId': '123456789012'}
            }
        ]
    }
    return sample_crawler_runs
