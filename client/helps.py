# -*- coding:utf-8 -*-
import re, json, io, urllib, hmac, hashlib

from xml.etree.ElementTree import Element, tostring
from ruamel.yaml import round_trip_dump, round_trip_load, load, dump_all

from bson.json_util import (default as bson_object_default,
                            object_hook as bson_object_hook)


def json_load(s):
    s = urllib.unquote(s)
    return json.loads(s, encoding='utf-8', object_hook=bson_object_hook)


def json_dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, default=bson_object_default,
                      encoding='utf-8')


def compute_x_token_sign(sign_key, access_token, msg_id, ttl):
    return hmac.new(str(sign_key), '{0}:{1}:{2}'.format(access_token, msg_id, ttl), hashlib.md5).hexdigest()


def compute_x_auth_sign(sign_key, msg_id, ttl):
    return hmac.new(str(sign_key), '{0}:{1}'.format(msg_id, ttl), hashlib.md5).hexdigest()


def dump_yaml_file(data, path, round_tripping=False):
    with io.open(path, 'w', encoding='utf-8') as writer:
        if round_tripping:
            round_trip_dump(data, writer, allow_unicode=True, )
        else:
            dump_all([data], writer, allow_unicode=True)


def load_yaml_file(path, round_tripping=False):
    data = None
    with io.open(path, 'r', encoding='utf-8') as reader:
        if round_tripping:
            data = round_trip_load(reader)
        else:
            data = load(reader)
    return data


def dict_to_xml(data=dict, root_tag=None, encoding='UTF-8'):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(root_tag)
    for key, val in data.items():
        child = Element(key)
        if isinstance(val, int):
            val = str(val)
        child.text = val
        elem.append(child)
    return tostring(elem, encoding=encoding)


def sorted_dict_values(adict):
    """
    将集合M内非空参数值的参数按照参数名ASCII码从小到大排序（字典序），使用URL键值对的格式（即key1=value1&key2=value2…）
    拼接成字符串
    """
    key_list = sorted(adict)
    data_str = ''
    for key in key_list:
        if adict[key]:
            data_str += key
            data_str += '='
            data_str += adict[key]
            data_str += '&'
    data_str = data_str[:-1]
    return data_str


def is_mongo_id(data):
    """
    验证mongoId格式
    """
    p2 = re.compile('^[a-z0-9]{24}$')
    return p2.match(str(data))


def is_timestamp(data):
    """
    验证时间戳格式
    """
    p2 = re.compile('\d{10}$')
    return p2.match(str(data))


def is_uuid(data):
    """
    验证UUID格式
    """
    p2 = re.compile('^[0-9a-zA-Z]{8}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{12}$')
    return p2.match(str(data))


def is_int(data):
    """
    验证是否为正整数
    """
    p2 = re.compile('^[0-9]\d*$')
    return p2.match(str(data))


def is_ok(regex, data):
    """
    验证是否符合正则规则
    """
    p2 = re.compile(regex)
    return p2.match(str(data))


def is_mobile(data):
    """
    验证是否为手机号
    """
    p2 = re.compile('^(0|86|17951)?(13[0-9]|15[012356789]|17[0-8]|18[0-9]|14[57])[0-9]{8}$')
    return p2.match(str(data))


def is_str(data):
    """
    验证是否为字母数字下划线-
    """
    p2 = re.compile('^[0-9a-zA-Z_-]*$')
    return p2.match(str(data))
