myset = {'apple','banana','cherry'}
myset2 = {'blackcurrat','mango','apple'}
myset2 = ['pineapple','mango']
for x in myset:
    print(x)
print('banana' in myset)
myset.add('orange')
myset.update(myset2)
set = myset.union(myset2)
print(set)
myset.remove('banana')
print(myset)

z = myset.intersection(myset2)
myset.symmetric_difference_update(myset2)
z = myset.symmetric_difference(myset2)
print(z)
print(myset)
z = myset.difference(myset2)
print(z)