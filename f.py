import pandas as pd
import numpy as np

favourite=pd.read_csv("./single/favourite.csv",engine='python',header=None,dtype=np.float32)
favourite=np.array(favourite).reshape([1,-1])[0].tolist()

content=[]
with open("./single/content.csv","r",encoding="utf-8") as f:
    line=f.readline()
    while(line!=""):
        content.append(line.replace("\n",""))
        line=f.readline()

print("Max:",max(favourite))
print("index:",favourite.index(max(favourite)))
print(content[favourite.index(max(favourite))])