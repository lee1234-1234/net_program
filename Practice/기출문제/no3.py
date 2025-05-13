# 주어진 문자열
url = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

# '?'로 나누어 쿼리 문자열 추출
query_string = url.split('?')[1]

# '&'로 나누어 각 키-값 쌍 추출
pairs = query_string.split('&')

# 딕셔너리 생성
result = {}
for pair in pairs:
    key, value = pair.split('=')
    result[key] = value

# 결과 출력
print(result)