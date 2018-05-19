# 字典
d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print(d['中国'])
    # del d[k] 删除d对应的值
    # k in d 是否在字典中
    # d.keys() 返回字典d中的所有键信息
    # d.values() 返回字典d中的所有值信息
    # d.items() 返回字典d中的所有键值对信息
print("中国" in d)

    # 函数操作方法
    # d.get(k,<default>) 键存在则返回相应值,不存在则返回<default>值
    # d.pop(k,<default>) 键存在则取出相应值,不存在则返回<default>值
    # d.popitem() 随机从字典中取出一个键值对,以元组形式返回
    # d.clear() 删除所有键值对
    # len(d) 返回字典元素个数

# 字典的操作
# 定义空字典d
d = {}
# 在d中新增两个键值对元素
d['a'] = 1
d['b'] = 2
# 修改第二个元素
d['b'] = 3
# 判断c是否是d的键
'c' in d
# 计算d的长度
len(d)
# 清空d
d.clear()