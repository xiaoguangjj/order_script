# -*- coding:utf-8 -*-
from collections import OrderedDict
import functools


def lru_cache(maxsize=100):
    """Least-recently-used cache decorator.

    Arguments to the cached function must be hashable.
    Cache performance statistics stored in f.hits and f.misses.
    http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

    """

    def decoration_fn(f):
        cache = OrderedDict()  # order: least recent to most recent

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            try:
                result = cache.pop(key)
                wrapper.hits += 1
            except KeyError:
                result = f(*args, **kwargs)
                wrapper.misses += 1
                if len(cache) >= maxsize:
                    cache.popitem(0)  # purge least recently used cache entry
            cache[key] = result  # record recent use of this key
            return result

        wrapper.hits = wrapper.misses = 0
        return wrapper

    return decoration_fn
