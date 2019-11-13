students_of_grade3_class2 = {}
while True:
    number_of_student = input("请输入学生学号:")
    if number_of_student == ("Q" or "q"):
        break
    else: 
        name = input("请输入学生姓名：")
        sex = input("请输入学生性别：")
        students_of_grade3_class2[number_of_student]={"name":name,"sex":sex}
        
for num,info in students_of_grade3_class2.items():
    print (num,info)