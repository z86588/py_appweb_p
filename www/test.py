#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a python module """

__author__ = 'Jack Zhang'

import dbhandler
from webObject import User, Blog, Comment


def test():
    yield from dbhandler.create_pool(user='www-data', password='www-data', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()


for x in test():
    pass
