# # sum of first 99 natural numbers
# from math import *
#
# list_1 = []
# # list.append(1)
#
# i = 0
# while i < 99:
#     i = i + 1
#     list_1.append(i)
#
# print(list)
#
# j = 0
#
# for k in list_1:
#     # print("{}{}".format("k is = ", k))
#     j = j + k
#     # print("{}{}".format("j is = ", j))
# print(j)
#
# b = 0
# for a in range(0,100):
#     b = b + a
# print(b)
#
# print(sum(range(0,100)))
#
# print("*********************************************")
#
#
# range_1 = range(0,100,10)
# print(list(range_1))
#
#
# n = 10
# while n > 0:
#     print(n*"*")
#     n = n - 1

# x = 5 % 2

# print(x)

# for o in range(1,11):
#     if o % 3 == 0 and o % 5 == 0:
#         continue
#
#     print(o)


print("*********************************************")

count = 0

while count < 10:

    n = int(input("Enter the number "))
    if n == 0:
        break

    else:
        if n % 3 == 0:
            continue
        else:
            print(n)

    count = count + 1

# fcatorial of a number

number = int(input("Enter the number to find factorial "))

i = number - 1
while i > 0:
    number = number * i
    i = i -1


print("{}{}".format('fact of number is ', number))









