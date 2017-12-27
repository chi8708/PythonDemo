# 打开一个文件 写入
fo = open("foo.txt", "w+")
print("文件名:", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 :", fo.mode)
fo.write("hello python")
fo.close()

# 打开一个文件 读取
fo = open("foo.txt", "r+")
str = fo.read(100)
print("读取的字符串是 : ", str)
fo.close()

import os
import sys
# os.rename("foo1.txt", "foo2.txt")
try:
    os.mkdir("testDir")
except Exception as e:
    print('创建目录失败:', e)
    t, v, tb = sys.exc_info()
    print('t', t, 'v', v)


print('当前目录:%s' % (os.getcwd()))
