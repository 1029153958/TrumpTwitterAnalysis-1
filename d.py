import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#处理发推数量变化

T=pd.read_csv("./single/time.csv",header=None)
T=np.array(T).reshape([1,-1])[0]

SUM=0;INIT=T[0]
x=[];y=[]
for t in T:
    SUM+=1
    x.append((INIT-t)/(1000*3600))
    y.append(SUM)

plt.plot(x,y)
plt.title("Trump's Twitter-Account Analysis")
plt.xlabel("Time(hour)")
plt.ylabel("TwittesNumber")
plt.show()
