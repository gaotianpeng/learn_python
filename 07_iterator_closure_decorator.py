import time
'''
01 迭代器
'''
print('迭代器-----------------------')
list_a = (1, 2, 3, 4)
it_test = iter(list_a)
print(next(it_test))
print(next(it_test))
print(next(it_test))
print(next(it_test))
# print(next(it_test)) # exception

'''
02 范围迭代器
'''
print('range iterator-----------------')
for i in range(10, 20, 1):
    print(i)

'''
03 自定义迭代器
'''
print('自定义迭代器--------------------')
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

for i in frange(10, 20, 0.5):
    print(i)

'''
04 lambda 表达式
'''
print('lambda 表达式-----------------')
def func_test(item):
    return item

a_dict = {'a':'aa', 'b':'bb'}

for i in a_dict.items():
    print(func_test(i))

b_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(b_list)
print(list(filter(lambda x:x>2, b_list)))

'''
05 闭包
'''
print('闭包-------------------------')
def func_common():
    a = 1
    b = 2
    return a + b

func_common()
# 内部函数引用外部变量
def def_closure(a):
    def add(b):
        return a + b
    return add

num1 = func_common()
print(type(num1))

num2 = def_closure(1)
print(type(num2))
print(num2(4))

# a*x + b = y
def a_line(a, b):
    def arg_y(x):
        return a*x + b
    return arg_y

line_a = a_line(3, 5)
print(line_a(2))

'''
06 装饰器
'''
print('装饰器-------------------------')

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间是 %s 秒' %(stop_time - start_time))
    return wrapper
@timer
def i_can_sleep():
    time.sleep(3)
i_can_sleep()

def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' %(argv, func.__name__))
            func(a, b)
            print('stop')
        return nei
    return tips

@new_tips('add_module')
def add(a, b):
    print(a+b)

@new_tips('sub_module')
def sub(a, b):
    print(a-b)

add(3, 2)
sub(3, 2)