# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:36:01 2023

@author: chris
"""
import os
import base64
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import smtplib
import ssl
class Mail:
    def __init__(self):
        self.port = 465
        self.server_domain_name= 'smtp@gmail.com'
        self.password = 'CR7bvb09'
        self.sender_mail = 'christoph.rehberg05@gmail.com'
    def send(self,emails,subject,content):
        ssl_context=ssl.create_default_context()
        service= smtplib.SMTP_SSL(self.server_domain_name,self.port,context=ssl_context)
        service.login(self.sender_mail,self.password)
        for email in emails:
            result = service.sendmail(self.sender_mail, email,f'Subject: {subject} \n {content}')
            service.quit()
        
mail = Mail()
mail.send('christoph.rehberg@gmx.net','Test','Was geht?')
