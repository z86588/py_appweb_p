#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   config_default.py
@Author  :   zgc_jack
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/6/10 21:39    1.0         None

describe:
"""

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'database': 'awesome',
    },
    'session': {
        'secret': '',
    }
}
