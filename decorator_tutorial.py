"""

"""
import functools


# Step One:
def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


def hello_world():
    print('hello world')


hello = my_decorator(hello_world)
hello()

# Step Two: Simple decorator
@my_decorator
def hello_world_2():
    print("hello world 2")


hello_world_2()


# Step Three: Decorator with parameter
def decorator_with_param(func):
    @functools.wraps(func)
    def wrapper(msg):
        print('wrapper of decorator with parameter')
        func(msg)
    return wrapper


@decorator_with_param
def hello_world_3(msg):
    print(msg)


hello_world_3('hello world 3')


# Step Four: Decorator with variable parameter
def decorator_with_var_param(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator with variable parameter')
        func(*args, **kwargs)
    return wrapper

@decorator_with_var_param
def hello_world_4(msg, count):
    print("{} {}".format(msg, count))


hello_world_4('hello world', 4)


# Step Five: Decorator with self define parameter
def repeat_call(num: int):
    def decorator_with_self_def_parameter(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(5):
                print('decorator with self define parameter')
                func(*args, **kwargs)
        return wrapper
    return decorator_with_self_def_parameter

@repeat_call(3)
def hello_world_5(msg, count):
    print("{} {}".format(msg, count))


hello_world_5('hello world', 5)

print(hello_world_5.__name__)





