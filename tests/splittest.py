#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyvideodismantling

# "D:/EV/报表1.mp4" 视频地址
# "D:/EV/123"  拆分图片存储地址

res=pyvideodismantling.split_action("D:/EV/报表1.mp4","D:/EV/123",6)

print(res)