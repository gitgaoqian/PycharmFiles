# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:46:23 2017

@author: ubuntu
"""

import keystoneclient.v2_0.client as ksclient

# Replace the method arguments with the ones from your local config
keystone= ksclient.Client(auth_url="http://192.168.1.50:9292",
                           username="admin",
                           password="admin",
                           tenant_name="admin")