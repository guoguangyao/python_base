#__author__ = "linnum"
#__time__ = "2019/11/17 10:35 AM"

'''
# del语句 删除
# 内存引用计数减1，至0则删除内存

del a  删除变量a   内存中的值不一定删除

None 空值对象
a = None 删除a变量中的内容， 接触a与所代表变量的绑定
其他语言中 会把a变量删除

'''

name01 = "八戒"
name02 = "悟空"
name02 = name01
del name01 # 删除变量name01, 此时打印会报错
name02 = None   # 为变量name02赋空值，此时打印会输出None

print(name01)

'''
核心数据类型
变量--存储对象的内存地址——比如空值对象 None

整型 int
整数：正数 复数 零

'''