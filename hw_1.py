#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:36:48 2021

@author: sage
"""
import requests
import base64

class Process():
    def __init__(self,origin):
        self.origin = origin
        self.result = dict

    def code(self):
        #opening with binary
        with open(self.origin, 'rb') as f:
            image_data = base64.b64encode(f.read())
        return image_data

    def respon(self):
        #getting response from API with access token
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=pSWNFiF13aVQUYFBuIohXTpg&client_secret=SNmYviIQUYiPb6k8frgHOKdkX51g2xlY'
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/colourize" 
        response = requests.get(host)
        params = {"image":self.code()}
        access_token = response.json()['access_token']
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        self.result = response

    def decode(self):
        #save the returned result as 1.jpg under the same folder
        data = self.result.json()['image']
        image_data = base64.b64decode(data)
        with open('1.jpg', 'wb') as f:
            f.write(image_data)


