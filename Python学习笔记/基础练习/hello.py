# coding=UTF-8

# def fun(args):
#     print (args,type(args))
#
# phone = ('13098765432', '16602700006', '18502799989')
# fun(phone)


# dict1 = {'name':'荸荠', 'age':30, 'work':'测试工程师'}
# print ('我的姓名是{name},我{age}岁,我是{work}'.format(**dict1))


# a = lambda a,b:a+b
# print (a(3,5))
#
# b = 1
# name = 'Bilon' if b == 1 else 'Foolish'
# print name

# import random
# li = []
# for i in range(6):
#     r = random.randrange(65, 91)
#     print chr(r)
#     li.append(chr(r))
# print (''.join(li))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = map(lambda a: a + 10, li)
print(list(result))