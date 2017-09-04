# -*- coding:utf-8 -*-
from werkzeug.local import LocalProxy
from werkzeug.contrib.cache import MemcachedCache as _MemcachedCache, text_type
from ..globals import config as globals_config

_memcached = None


class MemcachedCache(_MemcachedCache):

    def add(self, key, value, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        if isinstance(key, text_type):
            key = key.encode('utf-8')
        if self.key_prefix:
            key = self.key_prefix + key
        return self._client.add(key, value, timeout)


def _create_memecached():
    global _memcached
    if _memcached is None:
        _memcached = MemcachedCache(globals_config['memcached_servers'], key_prefix=globals_config['cache_key_prefix'])
    return _memcached

memcached = LocalProxy(_create_memecached)
