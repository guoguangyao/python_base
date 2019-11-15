#__author__ = "linnum"
#__time__ = "2019/11/16 7:05 AM"

'''
    汇率转换器
    输入美元，显示人民币
'''

# 1. 获取数据
str_usd = input("请输入美元：")
float_usd = float(str_usd)
# 2. 逻辑处理
rmb = float_usd * 7.0075

# 3. 显示结果
print(rmb)
