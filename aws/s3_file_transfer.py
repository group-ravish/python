import boto3

source_bucket_name = 'OpenInApp_Source'
destination_bucket_name = 'OpenInApp_Destination'


source_profile = 'OpenInApp_User1'
destination_profile = 'OpenInApp_User2'


source_session = boto3.Session(profile_name=source_profile)
source_s3_client = source_session.client('s3')

destination_session = boto3.Session(profile_name=destination_profile)
destination_s3_client = destination_session.client('s3')


file_content = source_s3_client.list_objects(Bucket=source_bucket_name)

for s3_object in file_content.get('Contents', []):
    key = s3_object['Key']


    destination_s3_client.copy_object(
        CopySource={'Bucket': source_bucket_name, 'Key': key},
        Bucket=destination_bucket_name,
        Key=key
    )

    print(f"Copied: {key} from {source_bucket_name} to {destination_bucket_name}")

print("Bucket Objects Copied Successfully!")