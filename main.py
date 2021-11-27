# Edit by Takeshi
dicts = open("dict.txt","r")
text = str(open("zhou.txt","r").read())
f = open("Answer.txt","w")
for line in dicts.readlines():
    line = line.split()[0]
    f.write(str(text.count(line.split()[0]))+" "+line+"\n")

f.close()
# # Edit by Takeshi
# from collections import OrderedDict
# dicts = open("dict.txt","r")
# text = str(open("zhou.txt","r").read())
# f = open("Answer.txt","w")
# seqdict = OrderedDict()
# for line in dicts.readlines():
#     line = line.split()[0]
#     seqdict[line] = text.count(line.split()[0])
    
# seqdict = OrderedDict(sorted(seqdict.items(), key=lambda t: t[1],reverse=True))
# print(seqdict)
# for dic in seqdict:
#     f.write(str(seqdict[dic])+" "+dic+"\n")

