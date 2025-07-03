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

#대입연산자
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
