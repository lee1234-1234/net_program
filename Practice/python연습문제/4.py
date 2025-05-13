# 문자 'a'가 들어가는 단어를 입력받아 처리하는 프로그램

# 사용자로부터 단어 입력 받기
word = input("Your word:")

# 'a'의 위치 찾기
index = word.find('a')

# 'a'가 단어에 포함되어 있는지 확인
if index != -1:
    # 첫 번째 줄: 'a'까지의 문자열 출력
    print(word[:index + 1])
    # 두 번째 줄: 나머지 문자열 출력
    print(word[index + 1:])
else:
    print("입력한 단어에 'a'가 포함되어 있지 않습니다.")
    
    
    
# 1부터 1000까지의 숫자의 각 자리수의 합 구하기
total_sum = 0
for num in range(1, 1001):
    for digit in str(num):
        total_sum += int(digit)

print("1부터 1000까지의 숫자의 각 자리수의 합:", total_sum)




# 0~49까지의 수로 구성되는 리스트
numbers = [i for i in range(50)]
print("0~49까지의 수로 구성된 리스트:", numbers)

# 0~49까지 수의 제곱으로 구성되는 리스트
squared_numbers = [i**2 for i in range(50)]
print("0~49까지 수의 제곱으로 구성된 리스트:", squared_numbers)