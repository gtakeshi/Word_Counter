# Edit by Takeshi
dicts = open("dict.txt","r")
text = str(open("zhou.txt","r").read())
f = open("Answer.txt","w")
for line in dicts.readlines():
    line = line.split()[0]
    f.write(str(text.count(line.split()[0]))+" "+line+"\n")

