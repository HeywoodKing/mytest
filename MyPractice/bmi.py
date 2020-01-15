import math

# height = 1.75
# weight = 80.5


h = input('请输入身高(m)：')
w = input('请输入体重(kg)：')

height = float(h)
weight = float(w)

bmi = weight/math.pow(height, 2)

if bmi < 18.5:
	print('指标BMI = %.2f 过轻' % bmi)
elif bmi >= 18.5 and bmi < 25:
	print('指标BMI = %.2f 正常' % bmi)
elif bmi >= 25 and bmi < 28:
	print('指标BMI = %.2f 过重' % bmi)
elif bmi >= 28 and bmi < 32:
	print('指标BMI = %.2f 肥胖' % bmi)
else:
	print('指标BMI = %.2f 严重肥胖' % bmi)


