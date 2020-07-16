#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def linear_search(li, value):
    for index, v in enumerate(li):
        if v == value:
            return index
    else:
        return None

