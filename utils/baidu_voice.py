# -*- coding:utf-8 -*-

import json
import logging
import requests
from requests.adapters import HTTPAdapter
# from cache_helper import memcached

BAIDU_OAUTH_CGI = "https://openapi.baidu.com/oauth/2.0/token/"
BAIDU_TEXT2VOICE_CGI = "http://tsn.baidu.com/text2audio"

_session = requests.session()
_session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
adapter = HTTPAdapter()
_session.mount('https://', adapter)
_session.mount('http://', adapter)
TIMEOUT = 5

logger = logging.getLogger(__name__)


def get_voice_access_token(api_key, secret_key):
    """
    获取百度语音Access Token
    :return:
    """
    # access_token = memcached.get("bd_voice_access_token")
    # if not access_token:
    return set_voice_access_token(api_key, secret_key)
    # return access_token


def set_voice_access_token(api_key, secret_key):
    """
    生成百度语音Access Token
    :return:
    :param api_key:
    :param secret_key:
    :return:
    """
    uri = BAIDU_OAUTH_CGI + "?grant_type=client_credentials&client_id={0}&client_secret={1}".format(api_key, secret_key)
    result = _session.get(uri)
    if result.status_code != 200:
        return False
    # 解析数据
    data = result.json()
    # memcached.add("bd_voice_access_token", data.get('access_token'), timeout=int(data.get('expires_in')))
    return data.get('access_token')