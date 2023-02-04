v1='a'
v2='1'
try:
    res=v1+v2
except TypeError:
    raise TypeError('Invalid parameters')
print(res)