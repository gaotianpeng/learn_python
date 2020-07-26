'''
01 条件语句
    if
    if else
    if elif
'''
# 条件语句
print('条件语句----------------------')
x = 'abc'
if x == 'abc':
    print('x = ' + x )
    print('x equals abc')

x = 'abcd'
if x == 'abc':
    print('x equals abc')
else:
    print('x = ' + x)
    print('x not equal abc')

# year = int(input('please input year of born:'))
year = 2019
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
if chinese_zodiac[year % 12] == '狗':
    print('狗年运势...')
elif chinese_zodiac[year % 12] == '马':
    print('马年运势力...')
else:
    print('不知道')

'''
02 for 循环语句
'''
# for 循环语句
print('for 循环语句----------------------')
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
for cz in chinese_zodiac:
    print(cz)

for i in range(13):
    print(i)
print('\n')
for i in range(1, 13):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

'''
03 while 循环语句
'''
import time

count = 1
while True:
    print(count)
    count += 1
    time.sleep(1)
    if count > 10:
        break