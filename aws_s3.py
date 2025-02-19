import boto3

def print_buckets():
    """
        Print all the S3 buckets in the account
    """
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(bucket_name):
    """
        Create a new S3 bucket
    """
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

def delete_bucket(bucket_name):
    """
        Delete an S3 bucket
    """
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)

def upload_file(bucket_name, file_name, object_name=None):
    """
        Upload a file to an S3 bucket
    """
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, object_name)