# lists [1,2,3,4,5,6]
# lists support indexing and slicing
my_list = ["kraken",'chutulu','dracula']
second_list = ['hume','descartes']
print(len(my_list))
#length of list
print(my_list[0])
# output will be kraken
print(my_list)
third_list = my_list + second_list
print(third_list)
third_list[0] = 'new addition to list'
print(third_list)
# lists can be manuplated unlike strings
third_list.append('kant') # appends method adds a new item in the brackets to end of the list
print(third_list)

#removing items from list

third_list.pop()  #pop removes the last item
print(third_list)
popped_item = third_list.pop()
print(popped_item) #outcome will be the last popped item (descartes)
print(third_list) #outcome will be without descartes
third_list.pop(0) #first item will be removed
print(third_list)

numbers_list = [0,999,3,0,0]
numbers_list.sort()
print(numbers_list)
numbers_list.reverse() #reverses the order of list
print(numbers_list)
h = numbers_list.count(0)
print(h)
