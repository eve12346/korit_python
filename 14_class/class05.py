#Account 클래스 => 계좌 정보
#owner 그리고 balance => 잔액은 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
#sithdraw 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
#만약 잔액이 부족하다면 출금을 할 수 없도록 출력

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def account1(self):
        print(f"{self.owner}님의 잔액은 {self.balance}원 입니다.")


    def deposit(self, deposit):
        self.balance = deposit
        print(f"입금된후 {self.owner}님의 잔액은 {self.deposit}원 입니다")

    def sithdraw(self, sithdraw):
        self.balance = sithdraw
        print(f"출금된후 {self.owner}님의 잔액은{self.sithdraw}원 입니다.")

account1 = Account("곽민성",100000)
account2 = Account("곽민성",150000)
account3 = Account("곽민성", 50000)

account1.introduce()