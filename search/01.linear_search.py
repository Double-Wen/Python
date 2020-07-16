#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 来自网易云课堂　https://study.163.com/course/courseMain.htm?courseId=1209405932


def linear_search(li, value):
    for index, v in enumerate(li):
        if v == value:
            return index
    else:
        return None

