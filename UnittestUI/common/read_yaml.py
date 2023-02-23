# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/22 18:50
# @Author :TGW
"""
import yaml


def load_yaml(text):
    with open(text,encoding='utf-8') as f:
        data = yaml.load(f,yaml.FullLoader)
    return data
