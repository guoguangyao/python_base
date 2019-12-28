#__author__ = "linnum"
#__time__ = "2019/12/28 11:31 PM


hour = int(input("请输入当前的小时？"))
minute = int(input("请输入当前的分钟？"))
second = int(input("请输入当前的秒数？"))

total_seconds = (hour * 3600) + (minute * 60) + second

print("当前共有" +  str(total_seconds) + "秒")
