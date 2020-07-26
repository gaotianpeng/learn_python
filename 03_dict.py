'''
01 dict
'''
print('dictionary --------------------------')
dict1 = {}
print(type(dict1))

tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)

'''
02 advance
'''
print('advance -----------------------------')
a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i*i)
print('a_list:')
print(a_list)

b_list = [i*i for i in range(1, 11) if i % 2 == 0]
print('b_lsit:')
print(b_list)

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
z_num = {}
for i in chinese_zodiac:
    z_num[i] = 0;
print(z_num)

z_num.clear()
z_num = {i:0 for i in chinese_zodiac}
print(z_num)


