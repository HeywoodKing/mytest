# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

# 导入Excel文档创建DataFrame对象
classmates = pd.read_excel('classmates.xlsx')
classmates.columns = ['id', 'name', 'age', 'gender']
print(classmates)

# 增加行
classmates.loc[5] = {
    'id': 16,
    'name': '安妮',
    'age': 34,
    'gender': '女'
}

classmates = classmates.append(pd.DataFrame([[100, '六大麻子', 32, '男']], columns=classmates.columns),
                               ignore_index=True)

# ignore_index表示索引重置
# ignore_index=True
print(classmates)


# 删除行
classmates = classmates.drop([5, 6])
print(classmates)


# 增加列
hobby = ['浪', '耍', '约', 'no', 'aa']
classmates['hobby'] = hobby
height = [170, 160, 165, 190, 175]
classmates.insert(2, 'height', height)  # 插入到第3列
print(classmates)


# # 删除列
# classmates = classmates.drop(['height'], axis=1)
# del classmates['hobby']  # 永久删除
# print(classmates)


# # 移动列
# gender = classmates.pop('gender')  # 先弹出
# classmates.insert(1, 'gender', gender)  # 再插入到适当位置
# print(classmates)


# # 排序
# # 按列排序
# classmates.sort_values(['name', 'age'], ascending=[0, 1])
# # 按索引排序
# classmates.sort_index()
# print(classmates)


# 拼接
friends = pd.DataFrame([['张三', '斯琴高兰', '博士', '西北华夏大学'], ['李四', '牛油果', '大专', '西安交通大学']],
                       columns=['name', 'nickname', 'edu', 'uni'], index=['zhangsan', 'lisi'])
classmates.index = ['zhangsan', 'lisi', 'wangwu', 'maliu', 'chenqi']
friends = friends.drop(['name'], axis=1)

# 使用concat 函数凭借，纵向拼接
oldguys = pd.concat([classmates, friends], axis=1, join='inner')
print(oldguys)


# 选取数据
# 下标索引，标签索引，布尔索引
# 查看形状
print(classmates.shape)
# 取前3行
print(classmates.head(3))
# 取后3行
print(classmates.tail(2))

# 选择多行
print(classmates[1:4])
print(classmates['lisi':'chenqi'])
# 提取一列返回Series
print(classmates.name)
# 提取多列
print(classmates[['name', 'age']])

# 用下标查看数据
print(classmates.iloc[0:2, :])
print(classmates.iloc[0:2])
print(classmates.iloc[0:5])
# # 用标签查看数据
# print(classmates.loc['lisi':'chenqi', :])
# # 布尔索引查看数据
# print(classmates[(classmates['age'] > 22) & (classmates.age < 27)])
# print(classmates[(classmates['age'] < 22) | (classmates.age > 27)])
# print(classmates[(classmates['age'] == 23)])
# print(classmates[classmates.age <= 30])

# 混合索引 不支持
# print(classmates[(classmates.iloc[0:4]) & (classmates.loc['lisi':'chenqi']) & (classmates.age <= 25)])


# 导出到csv文件
# classmates.to_csv('classmates.csv')


# 导出dataframe到Excel文件制定的sheet
# classmates.to_excel('my_classmates.xlsx', 'sheet2')


# 导出多个dataframe到同一个Excel表格多个sheet
# friends = classmates[0:1].copy()
# writer = pd.ExcelWriter('oldguys.xlsx')
# classmates.to_excel(writer, sheet_name='classmates')
# friends.to_excel(writer, sheet_name='friends')
# writer.save()


# 统计函数
dates = pd.date_range('20190101', periods=31)
df = pd.DataFrame(data=np.random.randn(31, 6), index=dates,
                  columns=['早晨', '上午', '中午', '下午', '晚上', '凌晨'])

# dates = pd.date_range('201901', periods=12)
# df = pd.DataFrame(data=np.random.randn(12, 6), index=dates,
#                   columns=['客户', '员工', '业绩', '满意度', '回报率', '财富值'])

df.describe()
print(df)

# 计算每日变化比例
dfchange = df.pct_change()
dfchange.fillna(0)
print(dfchange)

"""
count               非NA值的数量
describe            针对Series或DF的列计算汇总统计
min, max            最小值，最大值
idxmin, idxmax      最小值和最大值的索引值
quantile            样本分位数（0到1）
sum                 求和
mean                均值
median              中位数
mad                 根据均值计算平均绝对离差
var                 方差
std                 标准差
skew                样本值的偏度（三阶矩）
kurt                样本值的峰度（四阶矩）
cumsum              样本值得累计和
cummin, cummax      样本值的累计最小值和累计最大值
diff                计算一阶差分
pct_change          计算百分数变化
"""
