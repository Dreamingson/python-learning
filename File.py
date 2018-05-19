# 文件
    # 文件的打开模式
    # 'r' 只读模式，若文件不存在，则返回FileNotFindError
    # 'w' 覆盖写模式 文件不存在则创建，存在不则覆盖
    # 'x' 创建写模式 不存在则创建。存在则FileExistError
    # 'a' 追加模式 不存在则创建，存在则在文件最后追加内容
    # 'b' 二进制文件模式
    # 't' 文本文件模式
    # '+' 与r/w/x/a一同使用，在原功能基础上增加同时读写功能

    # 文件内容的读取
f = open("test.txt","w+")
f.write("中国是一个伟大的国家123")
    # <f>.read(size=-1) 读入全部内容                            
f.close()
f = open("test.txt")
s1 = f.read(2)
s2 = f.readline()
s3 = f.readlines()
print(s1,s2,s3)
f.close()

    # 逐行遍历全文本
filename = input()
fo = open(filename,"r")
for line in fo:
    print(line)
fo.close()

    # 数据的文件写入
    # f.write(str)
    # f.writelines(lines) 将列表写入文件
    # f.seek(offset) 改变当前文件指针位置 0 文件开头 1 当前位置 2 文件结尾

fo1 = open("output.txt","w+")
ls = ["中国","法国","美国"]
fo1.writelines(ls)
fo1.seek(0)
for line in fo1:
    print(line)
fo1.close()