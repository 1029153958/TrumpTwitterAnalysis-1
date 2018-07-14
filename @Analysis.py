def getWord():
    def normal(sentence,val=" "):
        sentence=sentence.lower()
        replace=["\n",":",".","/","\"","'","-","“","”","!"]
        for word in replace:
            sentence=sentence.replace(word,val)
        return sentence

    frequency = {}
    NOT_INTEREST=['@realdonaldtrump',]
    with open("./single/content.csv","r",encoding="utf-8") as f:
        line=f.readline()
        while(line!=""):
            words=normal(line).split(" ")
            for word in words:
                if(word!='' and word[0]=='@'and word not in NOT_INTEREST):
                    if(word in frequency):
                        frequency[word]+=1
                    else:
                        frequency[word]=1
            line=f.readline()
    return frequency


frequency=getWord()
dict= sorted(frequency.items(), key=lambda d:d[1], reverse = True)
for i in range(20):
    print(dict[i])