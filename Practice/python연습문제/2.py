# 친구 이름 리스트 작성
friends = ["kim", "lee", "bak"]

# insert()로 맨 앞에 새로운 친구 추가
friends.insert(0, "park")

# insert()로 3번째 위치에 새로운 친구 추가
friends.insert(2, "choi")

# append()로 마지막에 친구 추가
friends.append("jung")

# 결과 출력
print("친구 리스트:", friends)

# 리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
numbers = [1, 2, 3]

# 두 번째 요소를 17로 수정
numbers[1] = 17

# 리스트에 4, 5, 6을 추가
numbers.extend([4, 5, 6])

# 첫 번째 요소 제거
numbers.pop(0)

# 리스트를 요소 오름차순 정렬하기
numbers.sort()

# 리스트를 요소 내림차순 정렬하기
numbers.sort(reverse=True)

# 인덱스 3에 25 넣기
numbers.insert(3, 25)

# 결과 출력
print("숫자 리스트:", numbers)