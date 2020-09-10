import boto3
import botocore

BUCKET_NAME = 'raspbyprojectsdata'

get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

s3 = boto3.client('s3')
objs = s3.list_objects_v2(Bucket=BUCKET_NAME)['Contents']
LAST_ADDED_KEY = [obj['Key'] for obj in sorted(objs, key=get_last_modified, reverse=True)][0]
print(LAST_ADDED_KEY)

#KEY = 'raspbyprojectsdata/report/0_1599606370073.jsonl'

s3 = boto3.resource('s3')

try:
	s3.Bucket(BUCKET_NAME).download_file(LAST_ADDED_KEY, 'local_file.json')
except botobore.exceptions.ClientError as e:
	if e.response['Error']['Code'] == "404":
		print("The boject does not exist.")
	else:
		raise
