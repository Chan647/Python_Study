# format()함수 - 중괄호 안에 채우기
str_a = "{}".format(1000)
print(str_a, "\n")

str_b = '"내 나이는 {}"'.format(input("나이 : "))
print(str_b)
print(type(str_b),"\n")

format_a = "{} 만원".format(input())
print(format_a, "\n")

format_b = "{} 이다".format("나는")
print(format_b, "\n")

# format()함수 :d - 기능 기호나 공백 정수 추가하기
output_a = "{:d}".format(52)
output_b = "{:3d}".format(52)
output_c = "{:03d}".format(52)
print(output_a)
print(type(output_a))
print(output_b)
print(output_c)

# format()함수 :f 기능 - 부동 소수점 출력
#             :g 기능 - 의미없는 소수점 제거
output_d = "{:f}".format(52.273)
print(output_d)
output_f = "{:15f}".format(52.273)
print(output_f)
output_e = "{:15.2f}".format(52.273) # 15.2 -> 15칸을 채우되 소수점 아래 두칸 출력, 자동 반올림 됨 
print(output_e)

# upper(), lower() 함수 - 대문자,소문자로 변환
a = "helloworld"
print(a.upper())

# strip() 함수 - 공백 제거 
# lstrip - 좌
# rstrip - 우

# 문자열 구성 파악 - is--()함수

# find() 함수 - 문자열 찾기
# rfind() - 오른쪽에서 찾기

# 문자열과 in 연산자 - 문자열 내부에 찾고자 하는 문자가 있는지 확인(많이 쓰임)
october = "안녕하세요"
print("안녕" in october)

# split()함수 - 문자열 자르기
bc = "10 20 30".split(" ")
print(bc)

# f-문자열 - 문자열 내부에 표현식 추가
string_c = f"오늘의 날짜는 {18+1} 입니다."
print(string_c)