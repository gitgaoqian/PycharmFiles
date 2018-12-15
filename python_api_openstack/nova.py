# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:56:11 2017

@author: ubuntu
"""
import keystoneclient.v2_0.client as ksclient
import novaclient.v1_1.client as nvclient
# Replace the method arguments with the ones from your local config
keystone= ksclient.Client(auth_url="http://172.16.0.2:5000/v2.0",
                           username="admin",
                           password="admin",
                           tenant_name="admin")
nova_endpoint = keystone.service_catalog.url_for(service_type='compute',endpoint_type='publicURL')
nova=nvclient.Client(nova_endpoint,token=keystone.auth_token)
#instance=nova.servers.list  #为什么加上括号就不行了呢
#print instance

