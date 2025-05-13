days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 'December': 31
}

# 사용자로부터 월 입력받기
month = input("월을 입력하세요 (예: January 또는 Jan): ").strip()

# 월의 일수 출력
if len(month) == 3:  # 3자리 입력 (예: Jan)
    month_full = next((m for m in days if m.startswith(month)), None)
    if month_full:
        print(f"{month_full}의 일수는 {days[month_full]}일입니다.")
    else:
        print("잘못된 월 입력입니다.")
else:  # 전체 이름 입력 (예: January)
    if month in days:
        print(f"{month}의 일수는 {days[month]}일입니다.")
    else:
        print("잘못된 월 입력입니다.")

# 알파벳 순서로 모든 월 출력
print("\n알파벳 순서로 모든 월:")
for m in sorted(days.keys()):
    print(m)

# 일수가 31인 월 출력
print("\n일수가 31인 월:")
for m, d in days.items():
    if d == 31:
        print(m)

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍 출력
print("\n월의 일수를 기준으로 오름차순으로 (key-value) 쌍:")
for m, d in sorted(days.items(), key=lambda x: x[1]):
    print(f"{m}: {d}")