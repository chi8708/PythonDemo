import time
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import *


# 可选参数函数说明
def printinfo(arg1, *vartuple):
    print("输出:")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# lambad


def add(arg1, arg2): return arg1 + arg2


print(add(1, 2))

a = 0


def changeA():
    # 直接赋值无法修改全局变量，需要使用global
    global a
    a = 20
    print(a)


changeA()
print(a)

# time
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

print('时间格式化', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

runoob1()
runoob2()
