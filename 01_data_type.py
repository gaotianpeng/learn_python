'''
01 基本数据类型
    int     8
    float   8.8
    str     "8" "Python"
    bool    True/False
'''

# 判断类型
print('基本类型---------------')
print(type(1))
print(type(8.8))
print(type('8.8'))
print(type("8.8"))
print(type(True))

# 类型转换
print('类型转换---------------')
print(type(123))
print(type(str(123)))

'''
02 序列
    字符串    "abcd"
    元组      ("abc", "def")
    列表      [0, "abcd"]
'''
### 字符串
print('字符串---------------------------')
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
print(chinese_zodiac)
# 访问第1个元素
print(chinese_zodiac[0])
# 访问前4个元素
print(chinese_zodiac[0:4])
# 访问最后1个元素
print(chinese_zodiac[-1])
# 序列中是否有某元素
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
# 连接
print(chinese_zodiac + 'abcd')

### 元组:存储内容不可变更
print('元组------------------------------')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
print(type(zodiac_days))

print((1) < (2))
print((1,20) < (2,20))

a = (1, 3, 5, 7)
b = 4
print(list(filter(lambda x: x < b, a)))

### 列表:存储内容可变更
print('列表------------------------------')
a_list = ['abc', 'xyz']
print(a_list)
print(len(a_list))

a_list.append('x')
print(a_list)

a_list.remove('xyz')
print(a_list)
