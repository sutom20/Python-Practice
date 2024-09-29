#1 embedding a variable in string

name = 'sumit'
greeting = f"hello, {name} "


print(greeting)

name = "vishal"
greeting = f"hello, {name} "


print(greeting)


#2 using .format function

y = 10

greeting = "hello, {}{}{}"
with_name = greeting.format(name, ' ', y)
print(with_name)

x = 5

print('{}{}{}'.format(name, x, 5.5))

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx***************************")


#3 creating longer phases and using them at multiple places with multiple placeholders

longer_phrase = "Hello, {}. Today is {}. You are going to score {}."

runs = 100

formatted = longer_phrase.format('Sumit', 'a Good Day', runs)

print(formatted)
