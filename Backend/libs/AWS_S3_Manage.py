import boto3
from botocore.exceptions import ClientError


class S3:
    bucket_name = 'bucket-songzihan-test'
    s3 = boto3.resource('s3')
    s3_cli = boto3.client('s3')
    bucket = s3.Bucket(bucket_name)

    def __init__(self,username):
        self.username = username

    def get_bucket_info(self):
        """
        实例方法 获取桶内文件信息
        :return: 返回（对应username）的文件信息
        """
        file_list = []
        for obj in self.bucket.objects.all():
            file_list.append(obj.key)
        return file_list

    def upload_file(self,file,directory_name=''):
        """Upload a file to an S3 bucket

        :param file: File to upload
        :param directory_name: 文件放置的S3文件夹位置
        :return: True if file was uploaded, else False
        """
        complete_path = directory_name + file.filename

        # Upload the file
        s3_client = self.s3_cli
        try:
            # 第三个参数代表文件在bucket中的完整路径，包含文件名，例如 test/myfile.txt
            # response = s3_client.upload_file(file, self.bucket_name, complete_path)
            self.bucket.upload_fileobj(file,complete_path)
        except Exception as e:
            print(e)
            return False
        return True
