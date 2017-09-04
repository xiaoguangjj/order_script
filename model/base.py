# -*- coding:utf-8 -*-

from client import Client as seaguard_client
import config


class BaseModel(object):

    def __init__(self):
        self.client = seaguard_client(config.ACCESS_KEY, config.SECRET_KEY, api_gateway=config.AOAO_URI)
