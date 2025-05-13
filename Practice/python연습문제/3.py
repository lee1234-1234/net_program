from random import randint

# 게임 프로그램
def coin_game():
    money = 50
    print("게임 시작! 초기 금액: $50")
    
    while 0 < money < 100:
        guess = int(input("동전 앞면(1) 또는 뒷면(2)을 맞춰보세요: "))
        coin = randint(1, 2)
        
        if guess == coin:
            money += 9
            print("맞췄습니다! $9을 땄습니다. 현재 금액: ${}".format(money))
        else:
            money -= 10
            print("틀렸습니다! $10을 잃었습니다. 현재 금액: ${}".format(money))
    
    if money <= 0:
        print("돈을 모두 잃었습니다. 게임 종료!")
    else:
        print("축하합니다! $100을 달성했습니다. 게임 종료!")

# 최대 공약수 계산 프로그램
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 실행
if __name__ == "__main__":
    print("1. 동전 게임 실행")
    print("2. 최대 공약수 계산")
    choice = int(input("선택하세요 (1 또는 2): "))
    
    if choice == 1:
        coin_game()
    elif choice == 2:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        result = gcd(num1, num2)
        print("최대 공약수는 {}입니다.".format(result))
    else:
        print("잘못된 선택입니다.")