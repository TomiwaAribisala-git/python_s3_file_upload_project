import boto3 

def upload_to_s3(local_file, bucket, s3_file):
    """Uploading a local file into an s3 bucket using specified credentials."""
    ACCESS_KEY = "XXXXXXXXXXXXXXXXX"
    SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
# Using the upload_file method,
# local_file: path of the file to upload 
# bucket: name of the bucket to upload to 
# s3_file: name of the file in the bucket
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload successful")
        return True 
    except FileNotFoundError:
        print("The file was not found")
        return False

LOCAL_FILE = 'local_file_name'
BUCKET_NAME = 'my_bucket'
S3_FILE_NAME = 's3_file_name'
result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)