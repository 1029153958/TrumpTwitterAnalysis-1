import pandas as pd
import numpy as np

csv=pd.read_csv("./single/time.csv",header=None,dtype=np.float32)
T=np.array(csv).reshape([1,-1])[0]

#美国东部时间
#2009/5/5 2:54:25 第一条
#2018/7/13 1:53:20 最后一条
#共计34737条推特

print(T[0])
print(T[-1])
print(len(T))