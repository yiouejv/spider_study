#encoding: utf-8

import pandas as pd
import numpy as np


df = pd.read_csv('info.csv', encoding='gbk')
df.columns=['电影', '主演', '上映时间']
print(df)