#!/usr/bin/env python3
import json
import os
import requests
os.chdir(os.getcwd()+'/comments')
for file in os.listdir():
    comment_list = []
    key_list=['title','name','date','feedback']
    comment_dict={}
    print(os.getcwd())
    with open(file,"r") as f:
        for i in f :
            comment_list.append(i.strip('\n').strip('(\\)'))
        for (t,m) in  zip(key_list,comment_list):
            comment_dict[t]=m
    headers = {'Content-type': 'application/json'}
    rs = requests.post("http://104.196.110.84/feedback", json=comment_dict,headers=headers)
    print(comment_dict)
    print(rs)
    print(rs.request.body)




