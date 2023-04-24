# 如何处理异常
# try:
#   do something
# except ValueError as err:
#   handle err
# 注意except 只接受与它相匹配的异常类型并执行，如果程序抛出的异常并不匹配那么程序会退出

# 匹配多种异常
try:
    pass
except (ValueError, IndexError) as err:
    pass

try:
    pass
except IndexError as err:
    pass
except ValueError as err:
    pass

# Exception是所有非异常系统的基类，能够匹配任意非系统异常
# 也可在except后面省略类型，表示与任意异常匹配
try:
    pass
except:
    pass

# finally语法
try:
    pass
except:
    pass
finally:
    pass


# 自定义异常

class CustomExecption(Exception):
    # 异常初始化方法
    def __int__(self, value):
        self.value = value

    # 异常的string表达形式
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))

# raise 抛出异常
try:
    raise CustomExecption("22");
except CustomExecption as e:
    print(e)
