import pandas as pd
import numpy as np

retweet=pd.read_csv("./single/retweets.csv",engine='python',header=None,dtype=np.float32)
retweet=np.array(retweet).reshape([1,-1])[0].tolist()

content=[]
with open("./single/content.csv","r",encoding="utf-8") as f:
    line=f.readline()
    while(line!=""):
        content.append(line.replace("\n",""))
        line=f.readline()

print("Max:",max(retweet))
print("index:",retweet.index(max(retweet)))
print(content[retweet.index(max(retweet))])
