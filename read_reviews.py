import random

num = random.randint(1, 1000000)
data = []
count = 0
with open('reviews.txt', 'r')as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
            print(len(data))
# 随即留言
print(len(data))
print(num, data[num])
# 算平均留言长度
sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)
print('average is ', sum_len / len(data))
# 筛选清单1
new=[]
for d in data:
    if len(d)<100:
        new.append(d)
print(len(new))
#筛选清单2
good=[]
for d in data:
    if 'good' in d:
        good.append(d)
print(len(good))
#快写法
good=[d+'123' for d in data if 'good'in d]
bad=['bad'in d for d in data]
print(len(good))
print(bad)
