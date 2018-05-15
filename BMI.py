height,weight = eval(input("请输入身高(米)体重（千克）,用逗号隔开:"))
bmi = weight/(height**2)
status,props = " "," "
print(bmi)
if bmi < 18.5:
    status,props = "偏瘦","偏瘦"
elif bmi >= 18.5 and bmi < 24:
    status,props = "正常","正常"
elif bmi >= 24 and bmi < 25:
    status, props = "正常", "偏胖"
elif bmi >= 25 and bmi < 28:
    status, props = "偏胖", "偏胖"
elif bmi >= 28 and bmi < 30:
    status, props = "偏胖","肥胖"
else:
    status, props = "肥胖", "肥胖"

print("BMI指数为:国际'{0}',国内'{1}'".format(status,props))