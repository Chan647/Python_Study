# sys 모듈

import sys

print(sys.argv)

print("Wsversion : " , sys.getwindowsversion)
print("Copyright :", sys.copyright)
print("Version :", sys.version)

sys.exit

# os 모듈

import os

print(os.name)
print(os.getcwd())
print(os.listdir())

#os.mkdir("hi")
#os.rmdir("hi")
#os.rename("basic.txt", "test.txt")
#os.remove("test.txt")

os.system("dir")

# datetime 모듈
import datetime 

cur = datetime.datetime.now()
print(cur.year, "년")
print(cur.month, "월")
print(cur.day, "일")
print(cur.hour, "시")
print(cur.minute, "분")
print(cur.second, "초")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(cur.year,cur.month,cur.day,cur.hour,cur.minute,cur.second))

if cur.hour < 12 :
    print("현재 시간은 {}시로 오전입니다.".format(cur.hour))
else :
    print("현재 시간은 {}시로 오후입니다.".format(cur.hour))


import datetime

cur = datetime.datetime.now()

if 2 < cur.month < 6 :
    print("오늘은 {}월로 봄입니다.".format(cur.month))

elif 5 < cur.month < 9 :
     print("오늘은 {}월로 여름입니다.".format(cur.month))

elif 8 < cur.month < 12 :
     print("오늘은 {}월로 가을입니다.".format(cur.month))

elif 11 < cur.month < 3 :
     print("오늘은 {}월로 겨울입니다.".format(cur.month))

aft = cur + datetime.timedelta(weeks=1,days=1,hours=1,minutes=1,seconds=3)
print(cur.strftime("현재시간은 %Y{} %m{} %d{} %H{} %M{} %S{} 입니다.".format(*"년월일시분초")))
print(aft.strftime("현재시간은 %Y{} %m{} %d{} %H{} %M{} %S{} 입니다.".format(*"년월일시분초")))

a = cur.strftime("현재시간은 %Y{} %m{} %d{} %H{} %M{} %S{} 입니다.".format(*"년월일시분초"))
print(a)

b = cur.replace(year=(cur.year + 1))
print(b.strftime("현재시간은 %Y{} %m{} %d{} %H{} %M{} %S{} 입니다.".format(*"년월일시분초")))


# time 모듈(타이머)
import time
print("안녕하세요?")
time.sleep(5)
print("만나서 반갑습니다.")
