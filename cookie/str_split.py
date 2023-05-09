import re
# r'str' 防止转义
line = 'asdf fjdk; afed, fjek,asdf, foo'
# 正则标识切分
print(re.split(r'[;,\s]\s*', line))

# 字符串开头结尾匹配
# str.endswith()
# str.startswith()  还可以传入一个元组tuple
import os

listdir= os.listdir('.')

file=[file for file in listdir if file.endswith('.py')]
print(file)
# ?
print(any(file.endswith('py') for file in listdir))

# shell 通配符
from fnmatch import fnmatch,fnmatchcase
#  fnmatch函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式

# fnmatchcase函数使用模式大小写匹配

print(fnmatch("list.py", "*.py"))

