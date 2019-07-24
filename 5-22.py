#随机分配8个老师到3个办公室

import random

#定义老师和办公室
teachers = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh']
offices = [[],[],[]]

#每个办公室随机分两个
for officeNo in offices:
        while len(officeNo) < 2:
                teacherSum = len(teachers) - 1
                index1 = random.randint(0,teacherSum)
                officeNo.append(teachers[index1])
                del teachers[index1]

#随机分配剩下两个
for name in teachers:
    index2 =random.randint(0,2)
    offices[index2].append(name)

#输出
i = 1
for room in offices:
    print("办公室%d"%i)
    for teacherName in room:
        print(teacherName)
    print('-'*20)
    i += 1
