#__author__ = "linnum"
#__time__ = "2020/1/31 4:05 PM"

def fun01(a):
    print(a)
    print("fun01执行了")


b= 100
fun01(b)

 # 判断奇偶数

def  is_uneven(num):
     # 条件表达式
     # return True if num % 2 != 0 else False
    return num % 2 == 1


print(is_uneven(5))
print(is_uneven(6))

# 根据月，显示天数

def get_days_by_month(year, month):
    if month < 1 or month > 12:
        days = 0
        print("输入有误")
    elif month  ==  2:
        days = 29 if year  % 4 == 0 and year % 100 != 0 or year  % 400 == 0  else  28
    elif month in [4,6,9,11]:
        days = 30
    else:
        days = 31

    print(days)
    return days


get_days_by_month(2021,14)