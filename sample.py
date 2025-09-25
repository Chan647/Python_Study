number_list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dic = {}

for number in number_list:
    if number in dic:
        dic[number] += 1
    else :
        dic[number] = 1

print(dic)

print("사용된 숫자의 종류는 {}입니다".format(len(dic)))