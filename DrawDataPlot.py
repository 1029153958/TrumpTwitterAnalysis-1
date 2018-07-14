import matplotlib.pyplot as plt

# a=[1,3]
# b=["Indifferent","Positive"]
# plt.pie(a,labels=b,autopct='%1.2f%%',
#         explode=[0.1 for i in range(len(a))],shadow=True,pctdistance=0.8)
# plt.title("Twitter's Content Analysis - England")
# plt.axis('equal')
# plt.show()

# datas=[('@BarackObama', 702),('@FoxNews', 433),('@FoxAnd\nFriends', 419),('@Apprentice\nNBC', 377),('@Mitt\nRomney', 306),
#       ('@CNN', 256),('@Ivanka\nTrump', 186),('@Megyn\nKelly', 148),('@Sean\nHannity', 140),('@O\'Reilly\nFactor', 125)
#         ,('@Celeb\nApprentice', 122),('@NBC', 109),('@Trump\nDoral', 106),('@Macys', 106),('@Nytimes', 105),
#       ('@Eric\nTrump', 97),('@Greta\nWire', 90),('@Alexs\nAlmond', 90),('@Bill\nMaher', 85),('@NewsMax\nMedia', 83)]
#
# X=[i for i in range(20)]
# H=[data[1] for data in datas]
# Name=[data[0][1:] for data in datas]
#
# plt.bar([x for x in X],H,0.8)
# for i in range(20):
#     plt.text(X[i],H[i],Name[i],ha='center',va='bottom')
# plt.title("Trump Analysis - @")
# plt.show()

# a=[3,12,5,1]
# b=["Family","Politician","NewsReporter","Comedian"]
# plt.pie(a,labels=b,autopct='%1.2f%%',
#         explode=[0.1 for i in range(len(a))],shadow=True,pctdistance=0.8)
# plt.title("Trump Analysis - Character")
# plt.axis('equal')
# plt.show()

# a=[3,17]
# b=["Support","Oppose"]
# plt.pie(a,labels=b,autopct='%1.2f%%',
#         explode=[0.1 for i in range(len(a))],shadow=True,pctdistance=0.8)
# plt.title("Trump Analysis - Character")
# plt.axis('equal')
# plt.show()

# words=[('Obama', 1293),('America', 1065),('Barack\nObama', 708),('Hillary', 595),('#Trump\n2016', 571),('2016', 570)
#     ,('Interview', 562),('Job', 534),('FoxNews', 474),('World', 462),('Work', 455),('China', 450),('Apprentice', 446)
#     ,('Golf', 427),('FoxAndFriends', 426),('Clinton', 426),('American', 392),('CNN', 386),
#        ('#Make\nAmerica\nGreatAgain', 375),('Money', 352)]
#
# X=[i for i in range(20)]
# H=[word[1] for word in words]
# Name=[word[0] for word in words]
#
# plt.bar([x for x in X],H,0.8)
# for i in range(20):
#     plt.text(X[i],H[i],Name[i],ha='center',va='bottom')
# plt.title("Trump Analysis - Key Word")
# plt.show()


