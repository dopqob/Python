s = 'spam'
strlist = ['a', 'b', 'c']

s.find('pa')            # 搜索子字符串
s.strip()               # 移除空格(lstrip,rstrip)
s.replace('pa', 'xx')   # 替换
s.split()               # 通过指定分隔符对字符串进行切片
s.isdigit()             # 是否为纯数字
s.lower()               # 转换为小写
s.endswith('spam')      # 判断是否以‘spam’结尾
list(s)                 # 将字符串转换成列表
''.join(strlist)        # 把列表用分隔符连接成字符串
ord('a')                # 转换成对应的ASCII码
chr(115)                # 将ASCII码转换成对应的字符

# 转义字符：
# \\      反斜杠(\)
# \'      单引号(')
# \"      双引号(")
# \b      倒退
# \f      换页
# \n      换行
# \r      回车
# \t      水平制表符
# \v      垂直制表符