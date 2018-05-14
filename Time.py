import time
print(time.time()) # 时间戳
print(time.ctime()) # 年月日 字符串
print(time.gmtime()) # 计算机可用时间

# 时间格式化 strftime 时间-> 字符串
t = time.gmtime()
t1 = time.strftime("%Y-%m-%d %H:%M:%S",t) #%B 月份全称 %b 月份缩写 %A 星期全称 %a 星期缩写 %p上午下午
# %h 12h制 %H 24h制
print(t1)

# strptime 字符串 -> 时间
timeStr = '2018-05-14 04:30:40'
t2 = time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
print(t2)


# 程序计时
start = time.perf_counter()
time.sleep(5) # 程序休眠
end = time.perf_counter()
period = end - start
print(period)





