# {'key1':'value1','key2':value2'}
#dictionaries can not be sorted can retrieved by key
#lists can be sorted and can retrieved by location. ordered sequences
# can be indexed or sliced
# dictionaries retrieve value faster without location
my_dictionary =  {'key1':'value1','key2':'value2'}
print(my_dictionary)   #prints the whole dictionary
print(my_dictionary['key1']) #prints the value1

prices = {"180":'25000',"200":'28000',"220":'32500'}

a = input('bir model seçiniz')
print(prices[a]+"$")
print(type(a))
