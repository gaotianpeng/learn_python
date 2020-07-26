'''
01 异常处理
    try:
        <监控异常>
    except Exception [,reason]:
        <异常处理代码>
    finally:
        <无论异常发生是否都执行>
'''
try:
    year = int(input('input year: '))
except ValueError:
    print('年份要输入数字')
finally:
    print('finally')

try:
    print(1/0)
except ZeroDivisionError as e:
    print('0不能作为除数 %s' %e)

try:
    raise NameError('helloError')
except NameError:
    print('my custom error')