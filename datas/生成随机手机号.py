# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/21 13:38
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import random
i = 1000
d = []
for i in range(i):
    a = ["139","177","138"]
    b = random.choice(a)
    c = "".join(random.sample("0123456789",8))
    d.append(b+c)
print(d,len(d))
