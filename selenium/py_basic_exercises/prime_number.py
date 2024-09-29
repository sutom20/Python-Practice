
n = int(input('please enter the test number '))

i = 2
is_prime = True

while i < n:
    if n % i == 0:
        print('Given number is not prime')
        is_prime = False
        break

    else:
        i = i + 1

if is_prime:
    print('Given number is prime')

print('*******************************')












