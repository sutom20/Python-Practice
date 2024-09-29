scores = [99, 123, 600, 300, 202, 250, 303]

#find max of the above list

max_score = 0

for i in scores:
    if i > max_score:
        max_score = i

print(max_score)

print('################################################')

number_series = range(1,101)

for i in number_series:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    else:
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)


