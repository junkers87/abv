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
#width means the distance between the result was  and 0.13 strings
print('the result was {r:1.2f}'.format(r=result))


#f-strings
name = "jeremies"
print(f'his name is {name}')
a = "churchill "
b = "challenger "
c = "mathilda"
print(f'british main battle tanks are {a+b+c}')
om606 = '125Kw'
gtrg_grbx = '7 speed automatic gearbox'
print(f'New Mercedes C class has {om606} engine and {gtrg_grbx}')