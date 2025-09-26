
def prints() :
    print("-----Menu-----")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

class Account :
    def __init__(self, id , name, deposit, insert,withdrawl) :
        self.id = id
        self.name = name
        self.deposit = deposit
        self.insert = insert
        self.withdrawl = withdrawl
        

def sel() :
    selc = int(input("선택(1~5까지의 숫자만 입력) : "))
    return selc


prints()
id = []
name = []
deposit = []
withdrawl = []
insert = []
money = [deposit[i] + insert[i] - withdrawl[i] for i in range(len(insert))]

while True :
    selc = sel() 
    if selc == 1 :
        print("[계좌개설]")
        try : 
            Account.id = int(input("계좌ID: "))
            id.append(Account.id)
        except ValueError as ty :
            print("숫자를 입력하지 않았습니다.")
        pass

        try :   
            Account.name = (input("이름 "))
            name.append(Account.name)
         
        except TypeError as ty :
            print("문자를 입력하지 않았습니다.")
        try : 
            Account.deposit = int(input("입금액 "))
            deposit.append(Account.deposit)
            print(deposit)
        except ValueError as ty :
            print("숫자를 입력하지 않았습니다.")
        prints()

    elif selc == 2 :
        try :
            Account.id = int(input("계좌ID: "))
        except ValueError as ty :
            print("숫자를 입력하지 않았습니다.")

        try :  
            Account.insert = int(input("입금액 "))
            insert.append(Account.insert)
            
        except ValueError as ty :
            print("숫자를 입력하지 않았습니다.")

        print("입금완료")
        prints()

    elif selc == 3 :
        print("[출  금]")
        try : 
            Account.id = int(input("계좌ID: "))
            Account.withdrawl = int(input("출금액 "))
            withdrawl.append(Account.withdrawl)
        except ValueError as ty :
            print("숫자를 입력하지 않았습니다.")

        prints()

    elif selc == 4:
        print("계좌ID :" ,id[0],"\n", "이름 :" , name[0],"\n", "잔액 :", money[0])
        print("계좌id :" ,id[1],"\n","이름 :" ,name[1],"\n", "잔액 :", money[1])
        prints()

    elif selc == 5:
        break

    
