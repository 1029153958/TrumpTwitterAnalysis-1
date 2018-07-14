def normal(sentence, val=" "):
    sentence = sentence.lower()
    replace = ["\n", ":", ".", "/", "\"", "@", "'", "-", "“", "”", "!"]
    for word in replace:
        sentence = sentence.replace(word, val)
    return sentence

contents=[];INTRESTED=['finance','economy','']
with open("./single/content.csv","r",encoding="utf-8") as f:
    line=f.readline()
    while(line!=""):
        sentence=normal(line).lower()
        for KEY_WORD in INTRESTED:
            if(KEY_WORD in line):
                contents.append(line)
        line=f.readline()

for content in contents:
    print(content.replace("\n"," "))