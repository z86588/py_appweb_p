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
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore ' \
              'et dolore magna aliqua. '
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blog.html',
        'blogs': blogs
    }
