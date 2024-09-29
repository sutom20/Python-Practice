import random


# generates random integer number b/w a and b including a and b.

random_integer = random.randint(2, 3000)
print(random_integer)

# generates random floating number b/w 0 and 1 including 0. This is called the semi open range
random_number_0_to_1 = random.random()
print(random_number_0_to_1)


# generates random floating number b/w 0 and 1 including 0 -> multiply by 10 to extend the range from 1 to 10 exclusive of 10
random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

# generates random floating number b/w a and b including a and b.

random_float = random.uniform(2, 20)
print(random_float)

random_heads_tails_number = random.randint(0,1)
print(random_heads_tails_number)

if random_heads_tails_number == 0:
    print('Heads')
else:
    print('Tails')
