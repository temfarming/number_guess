import random

def game():
    choices = ['가위', '바위','보']
    wins, losses, ties = 0, 0, 0

    while True:

        while True:
            u_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
            if u_choice !=['가위' or '바위' or '보']:
                print("유효한 입력이 아닙니다")
                continue


            c_choice = random.choice(choices)

            print(f"사용자:{u_choice}, 컴퓨터: {c_choice}")


            if u_choice == c_choice:
                print("무승부!")
                ties += 1
            elif (u_choice == '가위' and c_choice == '보') or (u_choice =='바위' and c_choice == '가위') or (u_choice == "보" and c_choice == '바위'):
                print("사용자 승리!")
                wins += 1
            else:
                print("컴퓨터 승리!")
                losses += 1
                break

        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            break

    print("게임을 종료합니다")
    print(f"현재 전적 - 승: {wins}, 패: {losses}, 무승부: {ties}")

game()