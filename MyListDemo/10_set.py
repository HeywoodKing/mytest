# -*- coding: utf-8 -*-


days = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri'}
# print(days)
days.add('Sat')
# print(days)

# weeks = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
# print(weeks, type(weeks))
# a = weeks.pop()
# print(a, weeks)
# b = weeks.pop()
# print(b, weeks)

# weeks = set({'Mon', 'Tue', 'Wed', 'Thu', 'Fri'})
# print(weeks, type(weeks))
# weeks.add(12)
# print(weeks)
# weeks.add('Sat')
# weeks.add('Sun')
# print(weeks)
#
# # weeks.remove(12)
# # print(weeks)
#
# weeks.discard(12)
# print(weeks)

# for day in days:
#     print(day)

weeks = set([1, 2, 3, 'Sun', 'Sat'])
# 联合, 并集
res = days | weeks
print(res)

# 交集
res = days & weeks
print(res)

# 差集(只包含来自第一集合中的元素，不包含第二集合中的元素)
res = days - weeks
print(res)

res = weeks - days
print(res)


# 比较集合(检查给定的集合是否在另一个集合的子集或超集)
res = days > weeks
print(res)

res = weeks >= days
print(res)


# 这是字典定义不是集合
# weeks = ({})
# months = {}
# print(weeks, type(weeks), months, type(months))

