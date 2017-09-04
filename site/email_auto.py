#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

class Sendemail(object):
    smt_server = 'smtp.exmail.qq.com'   #服务器代理
    smt_port = 465
    smt_account = 'cs@cityio.cn'    #发送邮箱，密码
    smt_passport = 'Cs@123456'

    from_addr = smt_account

    def send_email(self,csvfile, title, to_addr=[]):
        """

        :param csvfile: file.csv
        :param title: subject
        :param to_addr: reciver
        :return:
        """
        self.msg = MIMEMultipart()
        fileopen = open(csvfile, 'r')
        self.att = MIMEText(fileopen.read(), 'base64')
        self.att["Content-Type"] = 'application/octet-stream'
        self.att["Content-Disposition"] = 'attachment; filename="' + str(csvfile.split('/')[-1]) + '"'
        self.msg.attach(self.att)

        self.msg['to'] = ';'.join(to_addr)
        self.msg['from'] = self.from_addr
        self.msg['subject'] = title
        try:
            self.server = smtplib.SMTP()
            self.server.connect(self.smt_server)
            self.server.login(self.smt_account, self.smt_passport)
            self.server.sendmail(self.msg['from'], to_addr, self.msg.as_string())
            self.server.quit()
        except Exception as e:
            print str(e)

if __name__ == '__main__':
    server = Sendemail()
    server.send_email('/data/shipment.csv', '安全达  骑士运单-收到请回复谢谢', ['zhouyan@cityio.cn','tianyi.li@meishisong.cn','xiaoguang.jing@cityio.cn'])
