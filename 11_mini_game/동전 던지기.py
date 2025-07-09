import random
import time

coin_sides = ["앞면", "뒷면"]
user_wins = 0
computer_wins = 0
rounds_played = 1

print("동전 던지기 게임이 시작되었습니다.")
while True:
    print(f"======round:{rounds_played}======")
    print("======현재 전적======")
    print(f"사용자: {user_wins}, 컴퓨터:{computer_wins}\n")

    user_guess = input("앞면과 뒷면중 하나를 선택해 주세요.(그만하려면 '종료'를 입력해 주세요):")
    if user_guess == "종료":
        print("======게임을 종료합니다.======")
        print(f"최종 전적은 사용자 {user_wins}승, 컴퓨터 {computer_wins}승 입니다.")
        print("============")
        break

    if user_guess not in coin_sides:
        print("앞면, 뒷면 또는 종료 중 하나를 정확히 입력해 주세요.")
        continue

    print("\n동전을 던집니다.....!")
    time.sleep(1)

    coin_result = random.choice(coin_sides)

    print(f"\n동전은 {coin_result}이(가) 나왔습니다!")

    if user_guess == coin_result:
        print("예측 성공! 맞추셨습니다!\n")

        user_wins += 1
    else:
        print(f"예측 실패! 아깝습니다.\n")
        computer_wins += 1

    rounds_played += 1

    if computer_wins == 5:
        print("======컴퓨터가 먼저 5승을 하였습니다======")
        break
    elif user_wins == 5:
        print("======유저가 5승을 하였습니다.======")
        break