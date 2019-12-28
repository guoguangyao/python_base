#__author__ = "linnum"
#__time__ = "2019/12/28 11:41 PM"

origin_weight = int(input("请输入两数"))
new_weight_jin = origin_weight // 16
new_weight_liang = origin_weight % 16

print("一共有" + str(new_weight_jin) + "斤" + str(new_weight_liang) + "两")