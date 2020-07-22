print('this is a string {}'.format('INSERTED'))
print('british main battle tanks are {2} {0} and {1}'.format('churchill' , 'challenger','mathilda'))
#british main battle tanks are mathilda churchill and challenger
print('british main battle tanks are {0} {0} and {0}'.format('churchill' , 'challenger','mathilda'))
#british main battle tanks are churchill churchill and churchill
print('british main battle tanks are {a} {b} and {b}'.format(a='churchill' , b='challenger',c='mathilda'))
#british main battle tanks are churchill challenger and challenger

result = 1/7.77
print(result)

print('the result was {}'.format(result))

#float formatting "{value:width.presicion f}"
print('the result was {r}'.format(r=result))