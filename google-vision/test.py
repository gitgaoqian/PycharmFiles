#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
# google api使用失败，主要可能是几个关键包的版本不对：google-api-core googleapis-common-protos google-cloud-dataproc等
import argparse
import io
import re
from google.cloud import vision



import os
import io
dir = '/home/ros/google-vision-api/First-Account-Key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=dir
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)
if __name__=='__main__':
    detect_labels('/home/ros/google-vision-api/huawei.jpeg')




