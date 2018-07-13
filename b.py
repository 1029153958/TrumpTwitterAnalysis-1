# -*- coding: UTF-8 -*-

#发帖时间、数量分析
#@分析
#常用词分析

#对中国的态度
#对盟友的态度
#对新闻媒体的态度
#金融看法

#相比其他Tweets的点赞数、转发数

LENGTH=34737

def getFavouriteNum():
    with open("./data/data.csv","r",encoding="utf-8") as O:
        with open("./single/favourite.csv","w",encoding="utf-8") as I:
            for i in range(LENGTH):
                line=O.readline()
                if(line!=[]):
                    single=line.split(",")
                    I.write(single[-1])

def getRetweetsNum():
    with open("./data/data.csv","r",encoding="utf-8") as O:
        with open("./single/retweets.csv","w",encoding="utf-8") as I:
            for i in range(LENGTH):
                line=O.readline()
                if(line!=[]):
                    try:
                        single=line.split(",")
                        I.write(single[-2]+"\n")
                    except IndexError:
                        print(i)

def getTime():
    with open("./data/data.csv","r",encoding="utf-8") as O:
        with open("./single/time.csv","w",encoding="utf-8") as I:
            for i in range(LENGTH):
                line=O.readline()
                if(line!=[]):
                    try:
                        single=line.split(",")
                        I.write(single[-3]+"\n")
                    except IndexError:
                        print(i)

def getContent():
    with open("./data/data.csv","r",encoding="utf-8") as O:
        with open("./single/content.csv","w",encoding="utf-8") as I:
            for i in range(LENGTH):
                line=O.readline()
                if(line!=[]):
                    try:
                        single=line.split(",")
                        I.write(single[1]+"\n")
                    except IndexError:
                        print(i)

getFavouriteNum()
getRetweetsNum()
getTime()
getContent()











