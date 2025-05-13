days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 'December': 31
}

print("\n알파벳 순서로 모든 월:")
for m in sorted(days.keys()):
    print(m)

for m, d in sorted(days.items(), key=lambda x: x[1]):
    print(f"{m}: {d}")

month = input("사용자 입력 : ").strip()

if len(month) == 3:
    month_full = next((m for m in days if m.startswith(month)), None)
    if month_full:
        print(f"{days[month_full]}")
    else:
        print("잘못된 월 입력입니다.")
else:
    if month in days:
        print(f"{month}의 일수는 {days[month]}일입니다.")
    else:
        print("잘못된 월 입력입니다.")

