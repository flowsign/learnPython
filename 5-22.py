import random
teachers=['11','22','33','44','55','66','77','88']
random.shuffle(teachers)
office1=teachers[:2]
office2=teachers[2:4]
office3=teachers[4:6]
office=[office1,office2,office3]

random.choice(office).append(teachers[6])
random.choice(office).append(teachers[7])

#输出
i = 1
for room in office:
    print("办公室%d"%i)
    for teacherName in room:
        print(teacherName)
    print('-'*20)
    i += 1