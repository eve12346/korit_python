#산술연산자
from runpy import run_path

num1 = 30
num2 = 12
print(f"num1 + num2 = {num1 + num2}")   #덧샘
print(f"num1 - num2 = {num1 - num2}")   #뺄샘
print(f"num1 * num2 = {num1 * num2}")   #곱샘
print(f"num1 / num2 = {num1 / num2}")   #나눗샘 (실수 몫)
print(f"num1 // num2 = {num1 // num2}") #나눗샘 (정수 몫)
print(f"num1 % num2 = {num1 % num2}")   #나눗샘 (나머지)

#대입 연산자
x = 10
x += 5 #x = x+5 => 15
x *= 2 #x = x*2 => 30
# x /= 5 #x = x/5 => 6.0
x //= 5 #x = x // 5 => 6

#비교 연산자
x = 10
y = 20
z = 10
print(x == z) #True
print(x >= y) #False
print(z == y) #False
print(x != z) #False
print(x <= y) #True
print(z >= z) #True

#논리 연산자
a = True
b = False
print(not a and b)  #False
print(a or b)       #True
print(not b)        #True

#조건 연산자(사망 연산자)

a = 10
b = 20
max_value = a if a > b else b
print(max_value)

#홀수 판별
num = 7
result = "짝수" if num % 2 == 0 else "홀수"
print(result)

#참일때 반환값 if 조건 else 거짓일때 반환값

