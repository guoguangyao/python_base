#__author__ = "linnum"
# #__time__ = "2020/2/9 3:39 PM"
#
# input_num = input('请输入一个数字：')
# if int(input_num) == 0:
#     print('Hello World')
# elif int(input_num) < 0:
#     for i in (0,len("Hello World")-1):
#         print("Hello World"[i])
#         i +=1
#         # TODO: write code...
# else:
#

n = int(input('enter a number: '))
str = 'Hello World'
if n == 0:
    print(str)
elif n < 0:
    for i in (0, len(str)-1):
        print(str[i])
        i = i + 1
elif n > 0:
    # print("Hello World"[0:2])
    # print("Hello World"[2:4])
    # print("Hello World"[4:6])
    # print("Hello World"[6:8])
    # print("Hello World"[8:10])
    # print("Hello World"[10:11])

    for x in range(len(str)):
        print(str[x:x+3])
        x = x +2