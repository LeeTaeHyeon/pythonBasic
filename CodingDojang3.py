"""
리스트[] 튜플() 딕셔너리 {}

## 변수 복사에 관해
    얕은복사 : 기존에 있는 메모리를 가르키기만 하는 복사 (원본에 영향을 준다)
    깊은복사 : 메모리를 새롭게 사용해 데이터를 복사 (독립된 변수이다)

## enumerate(iterable)
    인덱스와 함께 요소를 반환

## map
    리스트의 요소를 지정된 함수로 처리해서 맵 객체로 반환 해주는 함수
        list(map(함수, iterable))
    인풋에서도 활용 가능
        list(map(int, input().split()) # 스페이스바로 구문된 여러 숫자 입력 받을때

## 리스트와 튜플 응용하기
    리스트 : 여러가지 요소를 넣는다.
            mutable객체라 값을 변경해도 새로운 리스트를 만들지 않고, 기존 리스트를 변경
    튜플 : 리스트와 유사하지만 한번 초기화하면 변경이 불가능하다

##리스트 요소 추가
    list.append(element) : 리스트 끝에 "요소 하나"를 추가한다
    list.extend(list) : 리스트끼리 연결을 해준다.
    insert(index, element) : 원하는 인덱스에 요소를 넣는다.

##리스트 요소 삭제
    .pop(index) : 원하는 인덱스 요소 삭제 후 값 반환 / 안쓸경우 맨 마지막 값을 삭제
    .remove(element) : 특정 값을 찾아서 삭제

##리스트 메서드 들
    .index(element) # 해당 요소의 인덱스 값을 구하기
    .count(element) # 해당 요소 개수 구하기
    .reverse() # 순서뒤집기
    .sort() # 정렬 / 새로운 리스트를 만들때는 sorted()
    .min(), max(), .sum()

##리스트 슬라이싱
    list[start:end] end는 미포함


## tuple
    튜플 표현식을 사용할땐 앞에 tuple을 붙여줘야 한다. 안붙이고 ()만 쓰면 제너레이터
        tuple(결과값 for 변수 in 리스트) : 튜플 표현식
        (결과값 for 변수 in 리스트)  :제너레이터 표현식


## list comprehension
    리스트 안에 식, for문 if 조건문을 지정해서 리스트를 생성
    방법
        [결과값 for 변수 in 리스트]
        list(결과값 for 변수 in 리스트)

    [결과값 for 변수 in 리스트 if 조건문]
        리스트 -> 조건문 만족 -> 변수 -> 결과값 순으로 진행
    [결과값 for 변수 in iterator for 변수 in iterator]
        뒤쪽 for문 > 앞쪽 for문 > 결과값


## 2차원 리스트
    리스트 안에 리스트를 넣어서 구성
    list[row][col]로 요소에 접근한다
    2차원 list는 일반 copy가 아니라 deepcopy를 사용한다.

    for문 활용해서 꺼내기
        for i, i_value in enumerate(list):
            for j, j_value in enumerate(list[i]):
                print(list[i][j], end='')
            print()

    for문 활용해서 만들기
        a = []
        for i in range(3):
            line = []
            for j in range(2):
                line.append(j)
            a.append(line)

## dictionary
    키-값으로 이루어진 컨테이너

    딕셔너리 추가
        X.setdefault('key', default값)

    딕셔너리 수정
        X.update(키1=값1, 키2=값2) # 키에 해당하는 값을 수정, 키가 없다면 값을 추가, 여러개 가능

        update()할때 인자값으로 숫자, 리스트, 튜플 가능하다
            update([key, value], [key, value])
        update(zip([key list], [value list])로도 가능하다

    딕셔너리 삭제
        .pop(key, default) : key-value 값을 삭제하고, value 값을 반환
        del X[key]

    딕셔너리 키의 값 가져오기
        .get(key, default) : key에 해당하는 값 가져오기
        .items() : 키-값 쌍을 가져옴
        .keys() : 키를 모두 가져옴
        .values() : 값을 모두 가져옴

    리스트(튜플)로 딕셔너리 만들기
        dict.fromkeys(keylist, default)

    딕셔너리 출력
        for key, value in dictionary.items():
            ~~~

    딕셔너리 표현식
        딕셔너리에서 특정 값을 찾아 삭제할때 유용하다.
        for문을 돌면서 삭제하면 크기가 변경된다는 에러가 발생해서 안되고,
        표현식을 써서 삭제할 값을 제외하고 새로운 딕셔너리를 만드는것

    딕셔너리 안에 딕셔너리를 사용할수 있다.
    {key: {key: value}, key: {key: value}}

    딕셔너리는 반복문 사용하는 법이 중요하다.


## set
    중복을 허용하지 않고, 합집합 교집합 차집합등의 연산이 가능

"""

a = [10, 20, 30]
print(a)
print(len(a))

a.append(40)

print(a)
print(len(a))

a.append([400, 500])

print(a)
print(len(a))

a.extend([600, 700])

print(a)
print(len(a))

print(a.count(600))

print(a[2:5])

b = a

print(a is b)

c = a.copy()

print(a is c)
print(a == c)

for i in enumerate(a):
    print(i)

a.pop(4)

min_number = min(a)
max_number = max(a)

print(min_number, max_number)

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]

print(b)

a = [[10, 20], [30, 40], [50, 60]]

for i, i_value in enumerate(a):
    for j, j_value in enumerate(a[i]):
        print(i_value, j_value, end=' ')
    print()

a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(j)
    a.append(line)

print(a)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print(x.pop('z', 'no key'))

var = {key: value for key, value in dict.fromkeys(['a', 'b', 'c', 'd'], 0).items()}

print(var)

a = [1, 4, 3, 2]
a1 = a.sort()

print()
print(a)
print(a1)

print()

b = [1, 4, 3, 2]
b1 = sorted(b)
print(b)
print(b1)

