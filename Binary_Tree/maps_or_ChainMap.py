# Maps or ChainMaps in python.
# DS that handles combined dicts as it eliminates
# If there are duplicate keys, then the value from the
# first key is preserved.
import collections
dic1 = {'day1':'Mon','day2':'Tue'}
dic2 = {'day3':'Wed','day1':'Thu'}
res = collections.ChainMap(dic1,dic2)
# Creating single dictionary.
print(res.maps)
print('Keys = {}'.format(list(res.keys())))
print('values = {}'.format(list(res.values())))
# printing all elements.
for key, val in res.items():
    print('{} = {}'.format(key,val))
print()
# Finding a specific value in the result.
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}',format(('day4' in res)))
# Map reordering that behaves the same as the stacks.
res2 = collections.ChainMap(dic2,dic1)
print(res2.maps)