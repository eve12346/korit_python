#print(10/0)

try:
    print(10/0)
except:
    print("예외 발생!!")

try:
    num = int(input("숫자를 입력해 주세요:"))
    print(10/num)
except ValueError:
    print("문자말고 숫자를 넣어주세요.")
except ZeroDivisionError:
    print("0이외의 숫자를 넣어주세요")
