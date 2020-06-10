#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'

import asyncio
import dbhandler
from webObject import User, Blog, Comment


loop = asyncio.get_event_loop()


async def test():
    await dbhandler.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()


loop.run_until_complete(test())
