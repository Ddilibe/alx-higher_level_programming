#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

w = ['best','Best School 98 Battery street',"","z",'98']
for i in w:
    t = uppercase(i)
    print(t)
