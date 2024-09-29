#syntax -> [item1, item2, item3,....]
#can store mixed data types int, string, float, etc
#can alter/add/remove items from a list

import random

fruits = ['apple', 'orange', 'lichi']
fruits[1] = 'ORANGE'

print(fruits)

friends = ['A', 'B', 'C', 'D' , 'E']

pay_bill = random.choice(friends)
print(pay_bill)
