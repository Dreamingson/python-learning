# 集合
    # a = 'p'
    # A = {"python","123",("python","123")} #使用{}建立集合
    # B = set("python123")
    # print(A,B)

    # 集合间操作
    # S|T
    # S-T 在S中出现但没有在T中出现的元素
    # S&T
    # S^T
    # S < T || S <= T
    # S > T || S >= T

    # 增强操作符 更新集合S
    # S |= T
    # S -= T
    # S &= T
    # S ^= T

    # 集合处理方法
    # A.add(a) # 如果不存在a,那么添加a到A中
    # A.discard(a) # 移除a元素,如果不存在,不报错
    # A.remove(a) # 移除a元素,如果不存在,报错
    # A.clear() # 清空
    # A.pop() # 随机取出一个数
    # A.copy() # 返回一个副本
    # len(A) # 返回元素个数

    # 应用场景
    # 1.包含关系比较
    # 2.数据去重

# 序列(字符串,元组,列表类型)
    # 操作符
    # x in s
    # x not in s
    # s + t
    # s*n or n*s
    # s[i]
    # s[i:j] or s[i:j:k]

    # 函数方法
    # len(s)
    # max(s)
    # min(s)
    # s.index(x) 或 s.index(x,i,j) 从i到j第一次出现x的位置
    # s.count(x) 出现count的总次数

# 元组 创建后无法修改
creature = "dog","cat"
color = "blue", creature
print(color[1][1],color[::-1])

# 列表
    # ls[i] = x 替换第i个元素为x
    # ls[i:j:k] = lt
    # del ls[i] 删除第i个元素
    # del ls[i:j:k] 删除第i到j步长为k的元素
    # ls += lt 将列表lt增加到列表ls中
    # ls *= n 更新列表ls,其元素重复n次
ls = ["cat","dog","tiger",1024]
ls[1:2] = [1,2,3,4]
del ls[::3]
print(ls*2)
    # ls.append(x)
    # ls.clear() 删除所有元素
    # ls.copy() 生成一个新的列表,赋值ls中所有元素
    # ls.insert(i,x) 在i位置插入x元素
    # ls.pop(i) 从i位置取出对应元素并删除
    # ls.remove(x) 将第一次出现的x元素删除
    # ls.reverse() 将ls中的元素反转

lt = []
# 向lt新增5个元素
lt += [1,2,3,4,5]
# 修改lt的第二个元素
lt[1] = 6
# 在第二个位置增加一个元素
lt.insert(1,7)
# 第一个位置删除元素
del lt[0]
# 删除lt中第1-3位置的元素
del lt[0:3]
# 判断是否包含数字0
if 0 in lt:
    print("YES")
else:
    print("NO")
# 新增数字0
lt.append(0)
# 返回数字0所在lt中的索引
print(lt.index(0))
# lt的长度
print(len(lt))
# lt的最大元素
print(max(lt))
# 清空lt
lt.clear()
print(lt)

