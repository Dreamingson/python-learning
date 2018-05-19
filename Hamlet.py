def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
count = {}
for word in words:
    count[word] = count.get(word,0) + 1
item = list(count.items())
item.sort(key=lambda x:x[1],reverse=True) # 对第二个元素进行排序 True从大到小
for i in range(10):
    word,count = item[i]
    print("{0:<10}{1:>5}".format(word,count))