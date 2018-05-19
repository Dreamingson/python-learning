import os

# 文件管理
    # os.path.abspath(path) # 返回绝对路径
    # os.path.normpath(path) # 归一化path的表现形式，统一用\\分隔符
    # os.path.relpath(path) # 返回当前程序与文件的相对路径
    # os.path.dirname(path) # 返回path中的目录名称
    # os.path.basename(path) # 返回文件名称
    # os.path.join(path,*paths) # 组合path与paths,返回一个路径字符串
    # os.path.exits(path) # 返回目录是否存在
    # os.path.isfile(path) # 判断path对应是否已存在文件
    # os.path.isdir(path) # 判断path对应是否为已存在目录
    # os.path.getatime(path) # 返回上一次访问时间
    # os.path.getmtime(path) # 返回上一次修改时间
    # os.path.getctime(path) # 返回路径创建时间
    # os.path.getsize(path) # 返回文件对应大小

# 进程管理
    # os.system()

# 环境参数
    # os.chdir(path) # 修改当前程序操作的路径
    # os.getcwm() # 返回程序当前路径
    # os.getlogin() # 获取当前用户名
    # os.cpu_count() # 获取当前CPU数量
    # os.urandom(n) # 获得n个字节长度的随机字符串，通常用于加解密计算
    
