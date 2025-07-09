#사용자 정의 함수
#기본적인 사용자 장의 함수

# def plus(num1,num2):
#     print(num1 + num2)
#
# plus(5,8)
# plus(10,50)
#
# def hello(name):
#     print(f"안녕하세요.{name}님")
#
# hello("민성")

# def hello(name="홍길동"):
#     print(f"안녕하세요.{name}님")
# hello("민성")

#이름과 나이를 매개변수로 전달, 출력
#안녕하세요. 제 이름은 ***이고 나이는 ***입니다.

# def introduce(name, age):
#     print(f"안녕하세요. 제 이름은 {name}이고, 나이는 {age}입니다.")
# introduce("곽민성", 25)

#리턴값이 있는 사용자 정의 함수
# def plus(x,y):
#     return x + y
# result = plus(5,6)
# print(result)
#
# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(5))
#
# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(14))

# def cal_average(score_list):
#     total = sum(score_list)
#     return  round(total / len(score_list))
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 98, 95]
# score_list3 = [40, 90, 70]
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))

#매개변수로 단(구구단) 숫자를 전달하면 해당 구구단 출력
# def gugudna(num):
#     for i in range(1 , 10):
#         print(f"{num} * {i}= {num * i}")

# gugudna(3)

#콜백함수
#함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
#어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역할

# def calculator(x, y, operation):
#     return operation(x, y)
#
# def plus(x, y):
#     return x + y
# def minus(x, y):
#     return x - y
#
# def multiple(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print(calculator(3, 5, plus))
# print(calculator(3,10,minus))
# print(calculator(10,4,multiple))
# print(calculator(4,3,divide))
#
# import time
#
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머가 시작되었습니다.")
#     print(f"{pause_second}초 뒤에 함수가 실행됩니다.")
#
#     time.sleep(pause_second)
#
#     callback()
#     print("타이머가 종료되었습니다.")
#
# def hello():
#     print("안녕하세요.")
#
# timer(5,hello)

#lambda함수
#특정 범위 내에서만 사용되거나 호출되는 횟수가 한 번인 경우에 유용하게 사용되는 함수
#lambda 매개변수1, 매개변수2, ...: 함수 내부 코드

# def plus(x, y):
#     return x + y
# add_lambda = lambda x, y: x + y
# print(add_lambda(4,5))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map_result = map(lambda x: x * 2, numbers)
# list_result = list(map_result)
# print(list_result)

# def parity(num):
#     if num % 2 == 0:
#         return  "짝수"
#     else:
#         return "홀수"

parity = lambda num: "짝수" if num % 2 == 0 else "홀수"
print(parity(9))

#콜백함수 숫자 두개를 매개변수로 전달하고 해당 숫자 두개를 나누는 함수 정의
#나눠서 나머지가 0이면 True 0이 아니면 False => 삼항연산자

def calculator(x, y, operation):
    return operation(x,y)

def divide(x, y):
    return True if x % y == 0 else False

print(calculator(8,4,divide))

#매개변수로 리스트를 전달 받아서 해당 리스트의 요소가 짝수면 짤수, 홀수면 홀수
#바뀐 리스틀를 구하시고
num_list = [11, 16, 88, 75, 46, 97, 3, 14]
#result = ["홀수", "짝수", "짝수"...]
























