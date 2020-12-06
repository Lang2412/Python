# -*- coding = utf-8 -*-
# @Time : 2020/11/3 19:35
# @Author : 冯朗
# @File ： Normalization.py
# @Software : PyCharm

import sys

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print(' ')


# 水仙花问题
def jude(n):
    m = n
    a = int(m / 100)  # 百位
    if m % 100 >= 10:  # 对百取模，余下十位和个位
        m = m % 100
        b = int(m / 10)  # 十位
        m = m % 10  # 个位
    else:
        m = m % 100
        b = 0

    if pow(m, 3) + pow(a, 3) + pow(b, 3) == n:  # pow函数求幂
        return True
    else:
        return False


for i in range(100, 1000):
    if jude(i) == True:
        print(i, end=',')
print('end')


# python开发的学生信息管理系统
def showInfo():
    # 显示可以使用的功能列表给用户
    print("-" * 30)
    print("   学生信息管理系统   ")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.遍历学生信息")
    print("0.退出系统")
    print("-" * 30)


# 定义一个列表，用来存储多个学生的信息
students = []


def addStudent():
    stuName = input("请输入学生姓名:")
    stuId = input("请输入学生学号：")
    stuAge = input("请输入学生年龄：")
    # 验证学号是否唯一
    i = 0  # 记录要删除的下标
    leap = 0  # 标志位
    # 循环判断
    for stu in students:
        if stu['stuId'] == stuId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 1:
        print("输入学生的学号重复，添加失败！")
    else:
        stuInfo = {}
        stuInfo['stuName'] = stuName
        stuInfo['stuId'] = stuId
        stuInfo['stuAge'] = stuAge
        # 单个学生信息入表
        students.append(stuInfo)
        print("添加成功！")


# 删除学生信息
def deleteStudent():
    print("您选择了删除学生功能")
    delId = input("请输入要删除学生学号：")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == delId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 0:
        print("没有此学生学号，删除失败！")
    else:
        del students[i]
        print("删除成功！")


# 修改学生函数
def updateStudent():
    print("您选择了修改学生信息功能")
    alterId = input("请输入你要修改学生的学号")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == alterId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 1:
        updateOperate(stu)
    else:
        print("没有此学号，修改失败！")


def updateOperate(stuID):
    while True:
        alterNum = int(input("1.修改学号 \n2.修改姓名 \n3.修改年龄 \n4.退出\n"))
        if alterNum == 1:
            newId = input("请输入更改后的学号：")
            i = 0
            leap1 = 0
            for stu1 in students:
                if stu1['stuId'] == newId:
                    leap1 = 1
                    break
                else:
                    i = i + 1
            if leap1 == 1:
                print("输入学号不可重复，修改失败！")
            else:
                stu1['stuId'] = newId
                print("修改成功！")

        elif alterNum == 2:
            newName = input("请输入更改后的姓名：")
            stuID['stuName'] = newName
            print("修改成功！")

        elif alterNum == 3:
            newAge = input("请输入更改后的年龄：")
            stuID['stuAge'] = newAge
            print("修改成功！")

        elif alterNum == 4:
            break
        else:
            print("输入错误，请重新输入!")


# 查询单个学生信息
def getStudentById():
    print("您选择了查询学生信息功能")
    searchID = input("请输入要查询的学生的学号:")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == searchID:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 0:
        print("没有此学生学号，查询失败！")
    else:
        print("找到此学生，信息如下:")
        print("学号: %s\n姓名: %s\n年龄: %s\n" % (stu['stuId'], stu['stuName'], stu['stuAge']))


# 遍历所有学生信息
def getAllStudent():
    print("*" * 20)
    print("接下来遍历所有学生的信息...")
    print("学号       姓名      年龄")
    for stu in students:
        print("%s       %s      %s" % (stu['stuId'], stu['stuName'], stu['stuAge']))
    print("*" * 20)


# 主函数
def main():
    while True:
        showInfo()
        key = int(input("请选择功能："))

        if key == 1:
            addStudent()
        elif key == 2:
            deleteStudent()
        elif key == 3:
            updateStudent()
        elif key == 4:
            getStudentById()
        elif key == 5:
            getAllStudent()
        elif key == 0:
            quitconfirm = input("真的要退出吗？（yes or no)")
            if quitconfirm == 'yes':
                print("欢迎使用本系统，谢谢！")
                break
        else:
            print("您的输入有误，请重新输入")


main()
