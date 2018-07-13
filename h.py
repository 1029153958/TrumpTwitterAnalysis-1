import matplotlib.pyplot as plt

a=[1,3]
b=["Indifferent","Positive"]
plt.pie(a,labels=b,autopct='%1.2f%%',
        explode=[0.1 for i in range(len(a))],shadow=True,pctdistance=0.8)
plt.title("Twitter's Content Analysis - England")
plt.axis('equal')
plt.show()