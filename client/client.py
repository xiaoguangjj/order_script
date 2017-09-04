# -*- coding:utf-8 -*-
import requests
import inspect
from bson import ObjectId
from daisy.utils.datastructures import DotDict

from registry import Registry
from datetime import timestamp
from helps import load_yaml_file, json_dump, json_load, compute_x_auth_sign, compute_x_token_sign
import errors

_resource_registry = Registry()

HTTP_API_GATEWAY = 'https://seaguard.o3cloud.cn'

API_VERSION = '1.0'

CLIENT_VERSION = '0.0.1'

Q_PROTOCOL_PLAIN = 'plain'
Q_PROTOCOL_AES = 'aes'
Q_PROTOCOL_AES_BASE64 = 'aes-base64'
Q_PROTOCOL_OPTIONS = (Q_PROTOCOL_PLAIN, Q_PROTOCOL_AES, Q_PROTOCOL_AES_BASE64)

_api_errors = {}


def _load_error_maps():
    for k in dir(errors):
        cls = getattr(errors, k)
        if inspect.isclass(cls) and issubclass(cls, errors.ApiError):
            _api_errors[cls.code] = cls


_load_error_maps()


class ObjectResult(DotDict):
    object_cls = 'ObjectResult'

    def __init__(self, data, object_cls=None):
        if object_cls:
            self.object_cls = object_cls
        super(ObjectResult, self).__init__(**data)


class ObjectSetResult(object):
    def __init__(self, data, result_count=0, has_more=False):
        if not isinstance(data, list):
            data = list(data)
        self.data = data
        self.result_count = result_count
        self.at = 0
        self.has_more = has_more

    def __iter__(self):
        self.at = 0
        return self

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)

    def next(self):
        if self.at >= len(self.data):
            raise StopIteration
        doc = self.data[self.at]
        self.at += 1
        obj_cls = doc.pop('__type', None)
        return ObjectResult(doc, obj_cls)


def parse_result_meta(result):
    if not result:
        return result
    meta = result.get('_meta', {})
    if not meta:
        if isinstance(result, dict):
            return DotDict(**result)
        return result
    data = result.get('data')
    return ObjectSetResult(data, meta['result_count'], meta['has_more'])


def parse_errors(content):
    try:
        resp_data = json_load(content)
    except ValueError:
        raise errors.ApiError(message='Unknown api errors: %s' % content)
    # todo
    err_cls = _api_errors.get(resp_data['err_code'], errors.ApiError)
    raise err_cls(code=resp_data['err_code'], code_name=resp_data['err_name'],
                  message=resp_data['message'])


class Client(object):
    def __init__(self, access_key, secret_key, api_version=None, q_protocol=None, api_gateway=None, endpoint=None):
        self.access_key = access_key
        self.secret_key = secret_key
        if api_version is None:
            api_version = API_VERSION
        self.api_version = api_version
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Seaguard-Python/{0}'.format(CLIENT_VERSION)
        self.session.headers['Content-Type'] = 'application/json'
        if q_protocol is None:
            q_protocol = Q_PROTOCOL_PLAIN
        self.q_protocol = q_protocol
        if endpoint is None:
            endpoint = self.api_version
        if api_gateway is None:
            api_gateway = HTTP_API_GATEWAY
        self.base_endpoint = '/'.join([api_gateway, endpoint])

    def get_resource(self, name, namespace):
        return Resource(self, name, namespace)

    def __getattr__(self, item):
        resource_record = _resource_registry.get(item)
        if not resource_record:
            raise AttributeError('Unknown resource %s' % item)
        res = Resource(self, item, resource_record['route_base'], resource_record['apis'])
        setattr(self, item, res)
        return res

    def request_api(self, url_pattern, url_params, request_method, post_payload):
        if '{' in url_pattern:
            path_params = {}
            for k in url_params.keys():
                if k in url_pattern:
                    path_params[k] = url_params.pop(k, None)
            url = url_pattern.format(**path_params)
        else:
            url = url_pattern
        method = request_method.upper()
        session = self.session
        if post_payload:
            post_data = json_dump(post_payload)
        else:
            post_data = None
        msg_id = str(ObjectId())
        ttl = timestamp()
        headers = {
            'X-APP-KEY': self.access_key,
            'X-MSG-ID': '{0},{1}'.format(msg_id, ttl),
            'X-AUTH': compute_x_auth_sign(self.secret_key, msg_id, ttl) + ',master'
        }

        url = '/'.join([self.base_endpoint, url])
        try:
            resp = session.request(method, url, url_params, data=post_data, headers=headers)
            # print "RESP:", resp.content
            # print resp.headers
            if resp.status_code >= 400:
                parse_errors(resp.content)
            else:
                resp_data = json_load(resp.content)
            return parse_result_meta(resp_data)
        except:
            raise


class Resource(object):
    def __init__(self, client, name, resource_base, api_defines=None):
        self.route_base = resource_base
        self.client = client
        self.name = name
        if api_defines:
            self.apis = api_defines

    def __getattr__(self, item):
        api_info = self.apis.get(item)
        if not api_info:
            raise AttributeError('unknown api name: %s' % item)
        url = '/'.join([self.route_base, api_info['url']])
        url = url.replace('//', '/')
        method = api_info['method']

        def fn(params=None, **payload):
            return self.client.request_api(url, params, method, payload)

        setattr(self, item, fn)
        return fn

resource_yaml_name = '/'.join(__name__.split('.')[:-1]) + '/resources'

_records = load_yaml_file(resource_yaml_name + '.yml')

_resource_registry.extend(_records)

del _records
