import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#处理发推时间
T=pd.read_csv("./single/time.csv",header=None)
T=np.array(T).reshape([1,-1])[0]

Time=[]
for t in T:
    a=time.strftime("%H:%M",time.gmtime(float(t)/1000)).split(":")
    detailTime=int(a[0])*60+int(a[1])
    Time.append(detailTime)

PT={}
for i in Time:
    if(i in PT):
        PT[i]+=1
    else:
        PT[i]=1

x=[];y=[]
for V in PT:
    x.append(V)
    y.append(PT[V])

plt.bar(x,y)
plt.title("Trump's Twitter-Account Analysis")
plt.xlabel("<Morning>              Time(min)                 <Night>")
plt.ylabel("TweeterNumbers")
plt.show()
