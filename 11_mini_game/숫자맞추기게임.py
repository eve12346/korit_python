import random

difficulty_list = ["쉬움", "보통", "어려움"] #난이도 리스트
difficulty = ""   #입력받을 난이도 변수
max_try = 0 #최대 시도 횟수
max_range = 0 #최대 숫자 범위(범위가 클수록 난이도 증가)

while True: #난이도 선택 유효성 검사
    difficulty = input("난이도를 선택해 주세요.(쉬움, 보통, 어려움):")
    if difficulty in difficulty_list:
        break
    else:
        print("쉬움, 보통, 어려움 중에 선택해 주세요.")
        continue

if difficulty == "쉬움":
    max_try = 7
    max_range = 7

elif difficulty == "보통":
    max_try = 5
    max_range = 75

else:
    max_try = 3
    max_range = 100

correct_answer = random.randint(1, max_range)
try_count = 0 #시도한 횟수

while True:
    print(f"시도 횟수: {try_count}/{max_try}")
    if try_count >= max_try:
        print("시도 횟수를 초과하였습니다.")
        print(f"정답: {correct_answer}")
        break
    input_str = input("숫자를 맞춰보세요: ") #문자열

    if input_str.isdigit():
        guess = int(input_str)
    else:
        print("숫자로 입력해주세요.")
        continue

    if guess < 1 or guess > max_range:
        print("범위내의 숫자를 입력해 주세요.")
        continue

    if correct_answer > guess:
        try_count += 1
        print("정답은 더 높은 숫자 입니다.")
    elif correct_answer < guess:
        try_count += 1
        print("정답은 더 낮은 숫자 입니다.")
    else:
        print(f"정답입니다! {try_count}번 만에 맞추셨습니다.")
        break


print("======게임 종료 ======")