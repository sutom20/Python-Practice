def count(lst):
    ev = 0
    od = 0

    for i in lst:
        if i % 2 == 0:
            ev = ev + 1

        else:
            od = od + 1

    return ev, od


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even, odd = count(lst)

print("{}{}".format("Even count is ", even))
print("{}{}".format("Odd count is ", odd))


