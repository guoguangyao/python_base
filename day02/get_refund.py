#__author__ = "linnum"
#__time__ = "2019/12/28 11:15 PM"

item_price = float(input("请输入商品单价："))
item_amount = int(input("请输入商品数量："))
total_paid = float(input("请输入实付金额："))
refund = total_paid - (item_price*item_amount)
print("应找回" + str(refund))