# 递归算法

# reverse
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]

print(rvs("ertvrgh"))

# fibonacci
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(10))

# Tower of Hanoi
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(n,src,dst))
        count += 1
    else:
        hanoi(n-1 ,src ,mid ,dst )
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)

print(hanoi(3,'a','b','c'),count)
