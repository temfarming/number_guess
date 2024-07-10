import random

def number_guess():
    before_attempts = float('inf')

    while True:
        random_number = random.randint(1, 100)
        attempts = 0
        print(f"이전 게임 플레이어 최고 시도 횟수: {before_attempts if before_attempts != float('inf') else '없음'}")

        while True:
            try:                                            ## try - except 예외처리 추가 ##
                num = int(input("숫자를 입력하세요.: "))
                if num < 1 or num >100:
                    print("유효한 범위 내의 숫자를 입력하세요.")
                    continue
            except ValueError:
                print("유효한 숫자를 입력하세요.")
                continue

                attempts += 1

                if num < random_number:
                    print("업")
                elif num > random_number:
                    print("다운")
                else:
                    print("맞았습니다.")
                    print(f"시도한 횟수: {attempts}")
                    before_attempts = min(before_attempts, attempts)
                    break


        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("게임을 종료합니다.")
            break

number_guess()
