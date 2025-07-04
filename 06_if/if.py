#조건문
"""
if 조건:
    실행할 코드
"""
# num = int(input("숫자를 입력하세요:"))
# if num > 0:
#     print("양수 입니다")
# else:
#     print("음수입니다.")

#if - elif -else문
# score = int(input("점수를 입력하세요.:"))
# if score >= 90:
#     print("A학점입니다.")
# elif score >= 80:
#     print("B학점입니다.")
# elif score >= 70:
#     print("C학점입니다.")
# elif score >= 60:
#     print("D학점입니다.")
# else:
#     print("F학점입니다.")

#실습
#숫자를 입력받아서 조건문으로 홀짝 판별하기
# num = int(input("숫자를 입력하세요:"))
# if num % 2 == 0:
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")

#나이 입력받고, 학생여부 입력받기(Y/N)
#20세 이상이면서 학생이면 '성인학생입니다' 출력
#아니면 '성인학생이 아닙니다' 출력

age = int(input("나이를 입력하세요:"))
student = input("학생의 여부를 작성하세요(Y/N):")
if age >= 20 and student == "Y":
    print("성인 학생입니다.")
else:
    print("성인학생이 아닙니다.")

