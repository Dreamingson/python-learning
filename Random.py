import random
# 基本随机函数
random.seed(10) # 产生种子10对应的序列
print(random.random()) # 产生[0.0,1.0)之间的随机小数

# 拓展随机函数
a = 10
b = 100
print(random.randint(a,b)) # 生成一个[a,b]之间的整数

print(random.randrange(10,100,10)) # 生成一个[a,b]之间的随机整数, 步长为m

print(random.getrandbits(16)) # 产生一个k比特长的随机整数

print(random.uniform(a,b)) # 产生一个[a,b] 之间的随机小数random.uniform

seq = [1,2,3,4,5,6,7]
print(random.choice(seq)) # 从序列seq中随机选择一个元素

random.shuffle(seq)
print(seq) # 返回打乱后的序列 # 将seq中的序列随机排列,返回打乱后的序列