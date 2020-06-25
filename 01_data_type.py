'''
01 基本数据类型
    int     8
    float   8.8
    str     "8" "Python"
    bool    True/False
'''

# 判断类型
print(type(1))
print(type(8.8))
print(type('8.8'))
print(type("8.8"))
print(type(True))

# 类型转换
print(type(123))
print(type(str(123)))

'''
02 序列
    字符串    "abcd"
    列表      [0, "abcd"]
    元组      ("abc", "def")
'''
### 字符串
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

### 元组
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
print(type(zodiac_days))
