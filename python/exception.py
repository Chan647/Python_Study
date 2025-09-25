list = [52, 273, 32, 72, 100]

try : 
    number_input_a = int(input("정수 입력 :"))
    print("{}번째 요소 : {}".format(number_input_a +1,list[number_input_a]))
    예외.발생해주세요()


except ValueError as exc :
    print("정수를 입력해주세요")

except IndexError as exc :
    print("리스트의 인덱스를 벗어났어요")

except Exception as exc :
    print("미리 파악하지 못한 예외가 발생하였습니다.")
    print(type(exc), exc)



number = input("정수 입력")
number = int(number)

if number > 0 :
    raise NotImplementedError

else :
    raise NotImplementedError
    
