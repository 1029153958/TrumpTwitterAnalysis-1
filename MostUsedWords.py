def getWord():
    def normal(sentence,val=" "):
        sentence=sentence.lower()
        replace=["\n",":",".","/","\"","@","'","-","“","”","!"]
        for word in replace:
            sentence=sentence.replace(word,val)
        return sentence

    frequency = {}
    NotInterestWord=["","the","to","realdonaldtrump","a","is","i","of","in","and",
                     "you","for","on","com","be","http","s","trump","will","that",
                     "are","at","with","it","have","&","my","your","t","this","he",
                     "twitter","by","not","can","so","from","what","as","if","do",
                     "about","would","very","www","who","an","u","we","our","was",
                     "all","me","just","they","all","ly","get","should","https",
                     "am","over","re","their","go","being","want","or","she","day",
                     'his','out','donald','thank','thanks','people','new','like',
                     'has','no','now','run','one','more','make','up','when','today',
                     'us','how','why','only','m','need','going','pic','never','again',
                     'see','true','back','than','great','bit','time','big','but',
                     'don','best','via','love','think','vote','show','there','mr',
                     'last','been','him','much','really','must','watch','good',
                     'had','did','please','amazing','many','know','right','them',
                     'were','way','win','doing','\xa0…','ever','her','always',
                     'better','man','because','said','keep','years','hope','year',
                     'needs','deal','country','first','tonight','news','night',
                     'status','president','p','looking','even','business','apprenticenbc',
                     'obamacare','bad','poll','nice','donaldtrump','happy',
                     'national',]
    with open("./single/content.csv","r",encoding="utf-8") as f:
        line=f.readline()
        while(line!=""):
            words=normal(line).split(" ")
            for word in words:
                if(word not in NotInterestWord):
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