import boto3
from botocore.exceptions import ClientError

def calculate():
    with open("calculator-log.txt", "w") as file:
        while True:
            val = input("Enter first number: ")
            if val == "q":
                break
            val1 = input("Enter first number: ")
            if val1 == "q":
                break
            file.write(val + " + " + val1 + " = " + str((int(val) + int(val1)))+"\n")

def ex4():
    calculate()
    print('*** Uploading file to S3 ***')
    s3_client = boto3.client('s3')
    file = 'calculator-log.txt'
    bucket_name = 'sia-test-bucket'
    key_path = '2023/March/Meeting Minutes/notes.txt'
    try:
        response = s3_client.upload_file(file, bucket_name, key_path)
        print(response)
    except ClientError as e:
        print(e)
ex4()
