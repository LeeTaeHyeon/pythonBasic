# 파이썬 기초를 정리하는 공간입니다.

## for문은 반복 횟수가 정해져 있을때 사용한다.
### 구조 
```
  for loopIndex in iterable:  
      반복코드
```

### iterable 객체
  - range(start, end, step) (start <= x < end)
  - list, tuble, dictionary...

## while문은 조건에 따라서 반복이 필요할때 사용한다
### 구조
```
  while 조건문:
      반복코드
      조건 변화식 (없으면 무한루프)
```

## break, contunue로 반복문 제어 
보통 if 문과 많이 조합해서 사용한다.
- break : 반복문을 벗어날때 사용
- contunue : 반복문 내에서 코드 실행만 건너 뛸때
```
for i in range(1,10):
    if i == 5:
        break
        
    print(i)

while i < 10:
    if i % 2 == 0:
        continue
   
    print(i)
```

#리스트[] 튜플() 딕셔너리 {}

## 변수 복사에 관해
- 얕은복사 : 기존에 있는 메모리를 가르키기만 하는 복사 (원본에 영향을 준다)  
- 깊은복사 : 메모리를 새롭게 사용해 데이터를 복사 (독립된 변수이다)

## enumerate
- 인덱스와 함께 요소를 반환
```
    for index, number in enumerate(iterable):
        ~~~
```

## map
- 리스트의 요소를 지정된 함수로 처리해서 맵 객체로 반환 해주는 함수
```
    list(map(함수, iterable))
```

- 인풋에서도 활용 가능
```
    # 스페이스바로 구문된 여러 숫자 입력 받을때
        list(map(int, input().split()) 
```


## 리스트[]와 튜플()
- 리스트 : 여러가지 요소를 넣는다.  
  mutable객체라 값을 변경해도 새로운 리스트를 만들지 않고, 기존 리스트를 변경


- 튜플 : 리스트와 유사하지만 한번 초기화하면 변경이 불가능하다

### 리스트 요소 추가
    list.append(element) : 리스트 끝에 "요소 하나"를 추가한다
    list.extend(list) : 리스트끼리 연결을 해준다.
    insert(index, element) : 원하는 인덱스에 요소를 넣는다.

### 리스트 요소 삭제
    .pop(index) : 원하는 인덱스 요소 삭제 후 값 반환 / 안쓸경우 맨 마지막 값을 삭제
    .remove(element) : 특정 값을 찾아서 삭제

### 리스트 메서드 들
    .index(element) # 해당 요소의 인덱스 값을 구하기
    .count(element) # 해당 요소 개수 구하기
    .reverse() # 순서뒤집기
    .sort() # 정렬 / 새로운 리스트를 만들때는 sorted()
    .min(), max(), .sum()

### 리스트 슬라이싱
    list[start:end] # start <= X < end


## tuple ()
- 튜플 표현식을 사용할땐 앞에 tuple을 붙여줘야 한다.   
  안붙이고 ()만 쓰면 제너레이터  
```
    tuple(결과값 for 변수 in 리스트) : 튜플 표현식  
    (결과값 for 변수 in 리스트)  :제너레이터 표현식
```


## list comprehension
- 리스트 안에 식, for문 if 조건문을 지정해서 리스트를 생성
- 방법  
```
    [결과값 for 변수 in 리스트]
    list(결과값 for 변수 in 리스트)
```
```
    # 리스트 -> 조건문 만족 -> 변수 -> 결과값 순으로 진행
        [결과값 for 변수 in 리스트 if 조건문]
    
    # 뒤쪽 for문 > 앞쪽 for문 > 결과값
        [결과값 for 변수 in iterator for 변수 in iterator]
```

## 2차원 리스트
- 리스트 안에 리스트를 넣어서 구성
- list[row][col]로 요소에 접근한다
- 2차원 list는 일반 copy가 아니라 deepcopy를 사용한다.
```
    # for문 활용해서 꺼내기
        for i, i_value in enumerate(list):
            for j, j_value in enumerate(list[i]):
                print(list[i][j], end='')
            print()

    # for문 활용해서 만들기
        a = []
        for i in range(3):
            line = []
            for j in range(2):
                line.append(j)
            a.append(line)
```


## dictionary {}
- 키-값으로 이루어진 컨테이너
```
    X = {key: value, key: value}
```

- 딕셔너리 추가
```
    X.setdefault('key', default값)
    
    # 키만 지정하면 None값을 저장하고, default를 넣어주면 그 값이 들어간다
        X.setdefault('a')
           # X = {'a': None}
        X.sefdefault('b', 100)
           # x = {'a': None, 'b': 100}
```

- 딕셔너리 수정
```
    X.update(키1=값1, 키2=값2)
    
    # 키에 해당하는 값을 수정, 키가 없다면 값을 추가
        X.update(a=60, c=10)
            # X = {'a': 60, 'b': 100, 'c': 10}
  
     # update()할때 인자값으로 숫자, 리스트, 튜플 가능하다
        update([key, value], [key, value])
        update(zip([key list], [value list])
```
   
- 딕셔너리 삭제
```
    .pop(key, default)
    
    # key-value 값을 삭제하고, value 값을 반환, 없을경우 default
        X.pop('a')
            # 60
        X.pop('z', 0)
            # 0
            # X = {'b': 100, 'c': 10}    
        
    # key에 대한 값 삭제
        del X[key]
```
   
- 딕셔너리 키의 값 가져오기
```
    .get(key, default) : key에 해당하는 값 가져오기
    
    .items() : 키-값 쌍을 가져옴
        for key, value in X.items():
            ~~~
            
    .keys() : 키를 모두 가져옴
    
    .values() : 값을 모두 가져옴
```
   
- 리스트(튜플)로 딕셔너리 만들기
```  
    dict.fromkeys(keylist, default)
    
    # keylist의 요소로 key값을 만들고 default 값으로 value를 채운다
    
```

- 딕셔너리 표현식  
  - 딕셔너리에서 특정 값을 찾아 삭제할때 유용하다.  
  - for문을 돌면서 삭제하면 크기가 변경된다는 에러가 발생한다.    
  - 표현식을 써서 삭제할 값을 제외하고 새로운 딕셔너리를 만들어서 삭제 된것처럼 보이게 한다.  
```
    new_x = {key: value for key, value in X.items() if value != 20}
```

- 딕셔너리 안에 딕셔너리를 사용할수 있다.
```
    {key: {key: value}, key: {key: value}}
```
- 딕셔너리는 반복문 사용하는 법이 중요하다.


## set {}
- 순서가 없고, 중복을 허용하지 않는다.
- 합집합 교집합 차집합등의 연산이 가능
- index를 활용해 특정값을 못 뽑아낸다


- 값을 확인할때는 in 키워드
```
    'peach' in set
```

- iterable한 객체를 set() 함수에 넣으면 중복이 제거된 세트가 만들어진다
```
    a = set('apple')
        # a = {'e', 'l', 'a', 'p'}
```

- frozenset() 함수는 나중에 변경이 불가능하다  
일반적으로는 set안에 set를 넣지 못지만, frozenset을 활용하면 넣을수 있다.
```
    a = {{1, 2}, {3, 4}}
        # error
    frozenset({frozenset({1, 2}), frozenset({3, 4})})
        # 가능
```

- set 연산
  - 합집합(or)   
    set.union(set1, set2)  
    set1.update(set2)
  ```
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    set.union(a, b)
       #{1, 2, 3, 4, 5, 6}
  ```
  - 교집합(and)   
    set.intersection(set1, set2)  
    set1.intersection_update(set2)
  ```
    set.intersection(a, b)
        # {3, 4}
  ```
  - 차집합   
    set.difference(set1, set2)  
    set1.difference_update(set2)
  ```
    set.difference(a, b)
        # {1, 2}
  ```
  - 대칭차집합(XOR)  
    set.symmetric_difference(set1, set2)  
    set1.symmetric_difference_update(set2)
  ```
    set.symmetric_difference(set1, set2)
        # {1, 2, 5, 6}
  ```
  - 부분집합   
    set1.issubset(set2) : set1이 set2의 부분집합인가
  - 상위집합  
    set1.issuperset(set2) : set1dl set2의 상위집합인가
  - 같은지 다른지  
    set1 == set2
  - 세트가 겹치는지  
    set1.isdisjoint(set2)


- set 메소드
  - add(), remove(), discard(), pop(), clear()


- set 할당과 복사
  - set1 = set2 같은 객체이고
  - set2 = set1.copy() 다른 객체이다

- set 출력
  - 해오던대로 for i in set: ~~~
- set 표현식
  - 해오던대로 [i for i in 'apple' if i not in 'apl']