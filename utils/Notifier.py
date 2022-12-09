'''
@Description: notifications
@Author: Yang Boyu
@Email: bradleyboyuyang@gmail.com
'''

import json
import requests
import hmac
import hashlib
import base64
from urllib import parse
from datetime import datetime
import time



# robot webhook configuration
DD_ID = ''
DD_SECRET = ''


def cal_timestamp_sign(secret):
    """calculate timestamp for dingding robot"""
    timestamp = int(round(time.time() * 1000))
    secret_enc = bytes(secret.encode('utf-8'))
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    # 得到最终的签名值
    sign = parse.quote_plus(base64.b64encode(hmac_code))
    return str(timestamp), str(sign)

def send_dd_msg(content, robot_id=DD_ID, secret=DD_SECRET):
    """send dingding message to robot"""
    try:
        msg = {
            "msgtype": "text",
            "text": {"content": content + '\n' + datetime.now().strftime("%m-%d %H:%M:%S")}}
        headers = {"Content-Type": "application/json;charset=utf-8"}
        # https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        timestamp, sign_str = cal_timestamp_sign(secret)
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_id + \
              '&timestamp=' + timestamp + '&sign=' + sign_str
        body = json.dumps(msg)
        requests.post(url, data=body, headers=headers, timeout=10)
        print('Mobile message successfully sent')
    except Exception as e:
        print("Mobile message failed to be sent:", e)
