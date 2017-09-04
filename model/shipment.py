# -*- coding:utf-8 -*-
from base import BaseModel


class Shipment(BaseModel):

    def find(self, **kwargs):
        """

        :param kwargs:shipment
        :return:
        """
        print self.client.shipment.find(kwargs)
        return self.client.shipment.find(kwargs)
