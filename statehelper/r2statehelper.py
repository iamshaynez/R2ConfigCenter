import boto3
import os
import json

from dotenv import load_dotenv
load_dotenv()

class R2StateHelper:
    def __init__(self, cf_r2_account_id: str, cf_r2_access_key_id: str, cf_r2_secret_access_key: str, cf_r2_region: str, cf_r2_bucket_name: str) -> None:

        self.s3 = boto3.client(
            service_name ="s3",
            endpoint_url = f'https://{cf_r2_account_id}.r2.cloudflarestorage.com',
            aws_access_key_id = cf_r2_access_key_id,
            aws_secret_access_key = cf_r2_secret_access_key,
            region_name=cf_r2_region, # Must be one of: wnam, enam, weur, eeur, apac, auto
        )
        self.bucket_name = cf_r2_bucket_name
    
    def read_text(self, file_name: str):
        # 从 S3 获取文件对象
        response = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)
        # 读取内容
        content = response['Body'].read().decode('utf-8')
    
        return content


    def write_text(self, file_name, text_content):
        """
        将文本内容写入指定的 S3 存储桶中的文件。

        参数:
        file_name (str): 存储桶中文件的名称。
        text_content (str): 要写入的文本内容。
        """
        # 将文本写入 S3 文件
        self.s3.put_object(Bucket=self.bucket_name, Key=file_name, Body=text_content.encode('utf-8'))

    def read_json(self, file_name: str):
        """
        从指定的 S3 存储桶中读取 JSON 文件并返回 Python 字典。

        参数:
        file_name (str): 存储桶中文件的名称。

        返回:
        dict: JSON 文件内容转换成的字典。
        """
        # 从 S3 获取文件对象
        response = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)
        
        # 读取内容并解码为字符串
        content = response['Body'].read().decode('utf-8')
        
        # 将字符串解析为 JSON（字典）
        json_data = json.loads(content)
        
        return json_data

    def write_json(self, file_name, data):
        """
        将 Python 字典写入到指定的 S3 存储桶中的文件作为 JSON。

        参数:
        file_name (str): 存储桶中文件的名称。
        data (dict): 要写入的数据（字典格式）。
        """
        # 将字典转换为 JSON 字符串
        json_string = json.dumps(data)
        
        # 写入 JSON 到 S3 文件
        self.s3.put_object(Bucket=self.bucket_name, Key=file_name, Body=json_string.encode('utf-8'))

    """
    OPENAI Related
    """
    def read_openai_service(self, service_name: str):
        return self.read_json(f'openai_{service_name}.json')

    def write_openai_service(self, service_name, openai_base_url, openai_key):
        data = { "OPENAI_BASE_URL": openai_base_url, "OPENAI_API_KEY": openai_key}
        self.write_json(f'openai_{service_name}.json', data)

    """
    Telegram Bot Related
    """
    def write_tgbot(self, bot_name, bot_token, chat_id):
        data = {"TG_BOT_TOKEN":bot_token, "TG_CHAT_ID":chat_id}
        self.write_json(f'tgbot_{bot_name}.json', data)
    
    def read_tgbot(self, bot_name):
        return self.read_json(f'tgbot_{bot_name}.json')

def main():
    None

if __name__ == "__main__":
    cf_r2_account_id = os.environ['CF_R2_ACCOUNT_ID']
    cf_r2_access_key_id = os.environ['CF_R2_ACCESS_KEY_ID']
    cf_r2_secret_access_key = os.environ['CF_R2_SECRET_ACCESS_KEY']
    cf_r2_region = os.environ['CF_R2_REGION']

    state = R2StateHelper(cf_r2_account_id, cf_r2_access_key_id, cf_r2_secret_access_key, cf_r2_region, 'service-tokens')
    object_information = state.read_json('openai_zenuml.json')
    print(object_information)
    openai_json = state.read_openai_service('xiaowenz')
    print(openai_json['OPENAI_API_KEY'])
    tgbot_json = state.read_tgbot('iMessage')
    print(tgbot_json['TG_BOT_TOKEN'])
    #####
