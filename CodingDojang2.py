'''
for문은 반복 횟수가 정해져 있을때 사용한다.
구조
    for loopIndex in iterable:
        반복코드

iterable 객체
- range(start, end, step) (start <= x < end)
- list, tuble, dictionary...

while문은 조건에 따라서 반복이 필요할때 사용한다
구조
    while 조건문:
        반복코드
        조건 변화식 (없으면 무한루프)

break, contunue로 반복문 제어, 보통 if 문과 많이 조합해서 사용한다.
    break : 반복문을 벗어날때 사용
    contunue : 반복문 내에서 코드 실행만 건너 뛸때

'''

i = 2
j = 5

while i <= 32 or j >= 1:
    print(i, j)
    i = i * 2
    j = j - 1
