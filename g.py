content=[]
with open("./single/content.csv","r",encoding="utf-8") as f:
    line=f.readline()
    while(line!=""):
        sentence=(line.replace("\n"," ")).lower()
        if('russia' in line or 'frances' in line):
            content.append(line)
        line=f.readline()

print(len(content))
for i in content:
    print(i.replace("\n"," "))

#         总数 中立-反对-赞成
# China: 12 4-8-0
# 批评了奥巴马、布什，声明中国在非洲的军事威胁，抵制中国货

# Japna: 2 1-0-1
#共建更好的军事、新PPP协定

# Russina： 12 10-2-0
#双边关系、间谍事件、Russia and the world has already started to respect us again!

# England：4：1-0-3
#欢迎光临白宫、超级碗、英国趋势


