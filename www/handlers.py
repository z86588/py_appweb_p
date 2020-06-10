#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   handlers.py
@Author  :   zgc_jack
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/6/10 22:00    1.0         None

describe:
"""
import re, time, json, logging, hashlib, base64, asyncio
from webframe import get, post
from webObject import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users,
    }
