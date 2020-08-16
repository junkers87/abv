#tuples immutable unlike lists (items can not reassigned)
# tuples uses paranthesis
t = (1,2,3,2,2,2)
list_1 = [1,2,3]
print(type(list_1))
print(type(t))

print(t[0])

print(t.count(2))
print(t.index(3))
