# -*- coding: utf-8 -*-
"""
@author: Looking
@email: 2392863668@qq.com
"""
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import base64
import sys  
import codecs  

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())  
secret_key='xxxxxxx'
secretid='xxxx'
def tencentRecognition():
    # 通过本地语音上传方式调用
    try:

        # 重要：<Your SecretId>、<Your SecretKey>需要替换成用户自己的账号信息
        # 请参考接口说明中的使用步骤1进行获取。
        cred = credential.Credential(secretid,secret_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        clientProfile.signMethod = "TC3-HMAC-SHA256"
        client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile)

        # 读取文件以及base64
        with open("output.wav", 'rb') as f:
            data = f.read()
        base64Wav = base64.b64encode(data).decode()
        print("*************tencentRecognition begin......")
        # 发送请求
        req = models.SentenceRecognitionRequest()
        params = {"ProjectId": 0, "SubServiceType": 2, "EngSerViceType": "8k", "SourceType": 1, "Url": "",
                "VoiceFormat": "wav", "UsrAudioKey": "session-123", "Data": base64Wav}
        req._deserialize(params)
        resp = client.SentenceRecognition(req)
        print("************* tencentRecognition result:" + resp.to_json_string())
        return resp
        # windows系统使用下面一行替换上面一行
        # print(resp.to_json_string().decode('UTF-8').encode('GBK') )
    except TencentCloudSDKException as err:
        print(err)
