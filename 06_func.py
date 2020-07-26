'''
01 自定义函数
'''

print('自定义函数------------------')
def func(a, b, c):
    print('a= %s' %a)
    print('a= %s' %b)
    print('a= %s' %c)

func(1, 2, 3)

func(a=1, c=2, b=3)

def func_var_param(first, *other):
    print(1+len(other))

func_var_param(1, 2, 3)


print('变量作用域------------------')
var1 = 123
def func_scope():
    var1 = 456
    print(var1)

func_scope()
print(var1)

print('global 关键字--------------')
var1 = 123
def func_global_scope():
    global var1
    var1 = 456
    print(var1)
func_global_scope()
print(var1)


