# 字符串
# 通常有三种方式 ''  "" ''' '''或者""" """
# 支持三种方式为了方便字符串嵌套
str="I'm "
# 三引号主要用于多行字符
str1="""
 ONE
 TWO
 THREE    
"""

print(str1)

# 转义字符
# \newline => 下一行
# \\ => 表示\
# \' => 表示'
# \" => 表示"
# \n => 表示 换行
# \t => 表示 横向制表符
# \b => 表示 退格
# \v => 表示 纵向制表符
# \r => 表示 空格

# 字符串的常用操作 = > 字符串由单个字符组成的数组，所以可以像操作数组
# 一样操作字符串，另外字符串是不可变的

str1='Harden'
# 替换
new_str1='H'+str1[1:]

str1.replace('h','H')

# 优化
# Python 首先会检测 str1 还有没有其他的引用。如果没有的话，就会尝试原地扩充字符串 buffer 的大小
# 而不是重新分配一块内存来创建新的字符串并拷贝。这样的话，上述例子中的时间复杂度就仅为 O(n) 了。
s1='2'
s1+=s1 # => s1=s1+s1
print(s1)

# 其他函数 join() 拼接;split(separetor) 分割;
# strip(str) 去掉首尾字符串; lstrip(str) 去掉开头字符串; rstrip(str)去掉结尾字符串;
# find(sub,start,end) 查找

# 格式化
id=2
name='harden'
print('no data available for person with id: {}, name: {}'.format(id, name))
