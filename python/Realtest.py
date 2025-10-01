class Account:
    def __init__(self, acc_id, balance, name):
        self._acc_id = acc_id
        self._balance = balance
        self._name = name

    def get_acc_id(self):
        return self._acc_id

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        if self._balance < money:
            return 0
        self._balance -= money
        return money

    def show_info(self):
        print(f"계좌ID: {self._acc_id}")
        print(f"이름: {self._name}")
        print(f"잔액: {self._balance}\n")

acc_arr = []  

def show_menu():
    print("-----Menu-----")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

def make_account():
    print("[계좌개설]")
    try:
        acc_id = int(input("계좌ID:(숫자로 입력) "))
        name = input("이름: ")
        balance = int(input("입금액: "))
        print()
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다.\n")
        return

    acc_arr.append(Account(acc_id, balance, name))

def deposit_money():
    print("[입  금]")
    try:
        acc_id = int(input("계좌ID: "))
        money = int(input("입금액: "))
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다.\n")
        return

    for acc in acc_arr:
        if acc.get_acc_id() == acc_id:
            acc.deposit(money)
            print("입금완료\n")
            return
    print("유효하지 않은 ID 입니다.\n")

def withdraw_money():
    print("[출  금]")
    try:
        acc_id = int(input("계좌ID: "))
        money = int(input("출금액: "))
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다.\n")
        return

    for acc in acc_arr:
        if acc.get_acc_id() == acc_id:
            if acc.withdraw(money) == 0:
                print("잔액부족\n")
                return
            print("출금완료\n")
            return
    print("유효하지 않은 ID 입니다\n")

def show_all_acc_info():
    for acc in acc_arr:
        acc.show_info()

def main():
    MAKE, DEPOSIT, WITHDRAW, INQUIRE, EXIT = 1, 2, 3, 4, 5
    while True:
        show_menu()
        try:
            choice = int(input("선택(1~5까지의 숫자만 입력) : "))
        except ValueError:
            print("\n잘못된 선택\n")
            continue
        print()

        if choice == MAKE:
            make_account()
        elif choice == DEPOSIT:
            deposit_money()
        elif choice == WITHDRAW:
            withdraw_money()
        elif choice == INQUIRE:
            show_all_acc_info()
        elif choice == EXIT:
            break
        else:
            print("잘못된 선택\n")


if __name__ == "__main__":
    main()