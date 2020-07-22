#immutability: can not mutate/change
name = "sam"
# name[0] = 'p'
print(name)
last_letters = name[1:]
print("p" + last_letters)


x = "hello world "
print(x + 'its beautiful outside')

Y = x*10
print(Y)

print(x.upper())
# x. tab and you can see the methods usable on this string

x = "hi this is a string"

print(x.split())
#['hi', 'this', 'is', 'a', 'string']

print(x.split("i"))
#['h', ' th', 's ', 's a str', 'ng'] removes i and prints characters between "i"'s