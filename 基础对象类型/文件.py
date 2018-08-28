# 常见文件运算

output = open(r'C:\spam', 'w')      # 创建输出文件（'w'是指写入）
input = open('data', 'r')           # 创建输入文件（'r'是指读取）
input = open('data')                # 与上一行相同（'r'是默认值）
aString = input.read()              # 把整个文件读进单一字符串
aString = input.read(N)             # 读取之后的N个字节（一或多个）到一个字符串
aString = input.readline()          # 读取下一行（包括行末标识符）到一个字符串
aList = input.readlines()           # 读取整个文件到字符串列表
output.write(aString)               # 写入字节字符串到文件
output.writelines(aList)            # 把列表内所有字符串写入文件
output.close()                      # 手动关闭（当前文件收集完时会替你关闭文件）
output.flush()                      # 把输出缓冲区刷到硬盘中，但不关闭文件
anyFile.seek(N)                     # 修改文件位置到偏移量N处以便进行下一个操作
for line in open('data'):           # 文件迭代器一行一行的读取
    use line
open('f.txt', encoding='latin-1')   # Python 3.0 Unicode文本文件（str字符串）
open('f.bin', 'rb')                 # Python 3.0 二进制byte文件（bytes字符串）