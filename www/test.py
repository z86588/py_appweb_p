#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'

import dbhandler
import asyncio
from webObject import User, Blog, Comment


async def test(loop):
    await dbhandler.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

    dbhandler.__pool.close()
    await dbhandler.__pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
