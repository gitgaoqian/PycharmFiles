# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:14:18 2017

@author: ubuntu
"""
import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
# Replace the method arguments with the ones from your local config
keystone= ksclient.Client(auth_url="http://172.16.0.２:5000/v2.0",
                           username="admin",
                           password="admin",
                           tenant_name="admin")
glance_endpoint = keystone.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
glance=glclient.Client(glance_endpoint,token=keystone.auth_token)
image=glance.images.list()
print image
