def getNum():
    nums = []
    iNumber = input("请输入数字，回车退出")
    while iNumber != "":
        nums.append(eval(iNumber))
        iNumber = input("请输入数字，回车退出")
    return  nums


def mean(numbers): # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    m = s / len(numbers)
    return m


def dev(numbers,mean): # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev += (num-mean)**2
    return sdev/len(numbers)


def median(numbers): # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2+1])/2
    else:
        med = numbers[size//2]
    return med

def main():
    n = getNum()
    m = mean(n)
    p = dev(n,m)
    q = median(n)
    print("平均数:{} 方差:{} 中位数:{}".format(m,q,p))

main()
