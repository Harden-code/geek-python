# 函数定义
# def name(param1, param2, ..., paramN):
#     statements
#     return/yield value # optional


# 默认参数
def func(param=0):
    print(param)


# different isinstance() from type()
# type() 查看类型  isinstance() instance of

# 嵌套函数
# 好处：嵌套保护隐私
def f1():
    print('f1')

    def f2():
        print('f2')

    f2()


# 函数变量作用域
# 变量定义在函数内部就称局部变量，只在函数内部有效，一旦函数执行完毕，函数变量就会回收
# 全局变量->定义在整个文件层次上，但是不能在函数内部随意改变全局变量的值
# 因为python解析器会默认函数内部的变量为局部变量，如果想在函数内部修改全局变量就必须加global声明

INT_MIN = -1


def abs_err():
    INT_MIN = 1


abs_err()
print(INT_MIN)


# global 并不表示创建一个全局变量，而是告诉python解析器这个变量是之前定义的
def abs():
    global INT_MIN
    INT_MIN = 1


abs()
print(INT_MIN)


# nonlocal 关键字场景 在使用嵌套函数，内部函数可以访问外部函数定义的变量，但无法修改若要修改
# 就必须加上nonlocal
def out():
    str = 'out'

    def inner():
        # nonlocal str
        str = 'inner'
        print(str)

    inner()
    print(str)


out()


# 闭包
# 闭包跟嵌套函数类似的，不同的是外部函数返回一个函数，而不是具体的值

# 优点->函数开头需要做一些额外工作，而你又需要多次调用这个函数时，
# 将那些额外工作的代码放在外部函数，就可以减少多次调用导致的不必要的开销，提高程序的运行效率。
def power(exponent):
    def exponent_of(base):
        return base ** exponent;

    return exponent_of


square = power(2)

cube = power(3)
print(square, cube)

print(square(2))

# 匿名函数 lambda
# lambda argument1, argument2,... argumentN : expression
# lambda是一个表达式，并不是一个语句
# 表达式就是一系列公式去表达一个东西,比如x+2 x**2
# 语句则是完成某些功能，比如赋值，条件语句

# lambda可以用在一些常规函数def不能用的地方，比如
# (lambda x:x+1)(x) (x)调用函数
m = [(lambda x: x + 2)(x) for x in range(4)]

print(m)

# lambda 的主体只是一行简单表达式，并不能扩展成一个多行的代码块

# 函数 map(function, iterable) 的第一个参数是函数对象，第二个参数是一个可以遍历的集合，
# 它表示对 iterable 的每一个元素，都运用 function 这个函数。
import functools


def square(x):
    return x ** 2


squared = map(square, [1, 2, 3, 4, 5])
squared = map(lambda x: x ** 2, [1, 2, 3, 4, 5])

# 函数式编程
# 指代码中每一块都是不可变的，都是纯函数的形式组成，并且函数本身相互独立，互不影响
# 关于map()、filter() 和 reduce()三个函数，需要注意的是：
# 1.map()在 Python 2.x 返回的是一个列表；而在 Python 3.x 中返回一个 map 类，可以看成是一个迭代器。
# 2.filter()在 Python 2.x 中返回的是过滤后的列表, 而在 Python 3.x 中返回的是一个 filter 类，可以看成是一个迭代器，有惰性运算的特性, 相对 Python2.x 提升了性能, 可以节约内存。
# 3.reduce() 函数在 Python3 中已经被从全局名字空间里移除了，它现在被放置在 functools 模块里，如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数。
l = [1, 2, 3, 4, 5]
# map()
new_l = map(lambda x: x ** 2, l)
for e in new_l:
    print(e)
# filter() 过滤
l = [1, 2, 3, 4, 5]
filter(lambda x: x % 2 == 0, l)
# reduce() 计算列表元素的乘积
l = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, l)  # 1*2*3*4*5 = 120
print(l)

d = {'mike': 10, 'lucy': 2, 'ben': 30}
# new_d=dict(sorted(d.items(),key=lambda x:x[1]))
# for e in new_d.items():
#     print(e)
# dic items 返回元组的试图
for e in sorted(d.items(), key=lambda x: x[1]):
    print(e)
