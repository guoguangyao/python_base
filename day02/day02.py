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
# print(name01)

'''
核心数据类型
变量--存储对象的内存地址——比如空值对象 None

整型 int
整数：正数 复数 零

浮点数 float
小数（包含整数，复数，0.0）
科学计数法
'''

f01 = 1.0
print(f01)

f02 = 1.234e2
print(f02)

f03 = 1.234e-3
print(f03)

"""
# 复数 complex
# 由实部和虚部组成的数据
# 虚部是以j或J结尾
# 字面值： 1j  1+1j  1-1j
"""

c01 = 1j
c02 = 5+1j
print(c02)
print(type(c01))

"""
布尔值


数据类型转换
"""
str_scor = input("请输入成绩：")

print(type(str_scor))

i01 = int("3")  # 如果需要转换的类型和，与目标类型不一致，则错误
i01 = float("3.2")  # 如果需要转换的类型和，与目标类型不一致，则错误

"""
练习：在控制台中录入学生信息（姓名，年龄，性别，成绩）
在一行输出
格式：我的姓名是：XXX，年龄是：XXX，性别是：XXX，成绩是：XXX
"""

str_name = input("请输入姓名：")
str_age = input("请输入年龄：")
str_gender = input("请输入性别：")
str_grade = input("请输入成绩：")
print("-------------------------------------------")
print("我的姓名是："+str_name)
print("我的年龄是："+str_age)
print("我的性别是："+str_gender)
print("我的成绩是："+str_grade)

# 变量命名规则  str_name  类型_名字  一定要起的有意义