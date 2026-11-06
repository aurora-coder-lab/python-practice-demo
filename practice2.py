#定义总工资为10000元
cash = 10000

#逐行排序20名员工
for num in range(1, 21):

    #随机绩效分
    import random
    score = random.randint(1, 10)

    #判断绩效分是否大于5：

    #绩效分小于5时
    if score < 5:
        print(f"员工{num},绩效分{score},低于5,不发工资,下一位。")

    #绩效分大于5时
    else:
        cash -= 1000
        print(f"向员工{num}发放工资1000元，账户余额还剩{cash}元")
    if cash <= 0:
        print("工资发完了，下个月领取吧")

        #结束循环
        break