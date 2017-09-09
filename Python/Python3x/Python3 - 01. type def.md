# Python3

## TPYE

### 숫자

- `+` `-` `*` `/` `%`는 java와 같음
- `a ** b` : a의 b승
- `a // b` : a를 b로 나눈 후 소수점은 버림



### 문자열

- char형이 따로 없다
- 이스케이프 코드
  - `\n` : 줄바꿈
  - `\r` : 캐리지 리턴. 줄바꿈 후 커서를 바뀐 줄로 위치시킨다.
  - `\000` : null 문자
  - `\t` : 수평 탭
  - `\"` : 큰따온표 출력

``` python
# 문자열 종류
str_a = "큰 따온표 입력"
str_b = "작은 따온표 입력"
str_c = """큰 따온표 3개.
줄 바꿈도 인식한다.
"""

# 문자열 더하기
str_concat1 = "Hello"
str_concat2 = " World"
str_add = str_concat1 + str_concat2

# 문자열 곱하기
str_ㅡmulti = "Hello" * 3

# 문자열에도 인덱스가 있다.(음수는 뒤에서부터)
str = "20170831010230"
str[0] + str[1] + str[2] + str[3]
str[-4] + str[-3] + str[-2] + str[-1]

# 문자열 슬라이스
str[3:8]  # 원하는 구간을 슬라이스
str[:8]  # 시작 생략 가능
str[8:]  # 끝 생략 가능
str[:]  # 전부 출력

# 문자열 교체.  문자열 튜플 자료형은 그 요소값을 변경할 수 없다.
str1 = "ABCD"
str1[1]

str[1] = "F"
print(str1)  # ERROR

str1[:1] + 'F' + str1[2:] # OK
```



문자열 format

``` python
""" Format code
%s : 문자열(String),
%c : 문자(character)
%d : 정수(Integer)
%f : 실수(Float)
%o : 8진수
%x : 16진수
%% : 리터럴 %
%0.2f : 소숫점 표현하기(소숫점 2자리까지 표현)
%10s  : 10자리의 공간을 만든 후 오른쪽 정렬(음수는 반대)
"""

# example code
day = 31
name = "HJ"
percent = 100
decimal_point = 2.454545

print("오늘은 %d일이고, 제 이름은 %s입니다." %(day, name))
print("성공할 확률은 %d%% 입니다" %percent)
print("%0.2f " %decimal_point)
print("%10s" %name)
print("%-10s" %name)
```



문자열 자주 사용하는 함수

``` python
# 문자열 자주 사용하는 함수
abc = "hello"

# 대문자로
abc = abc.upper()
print(abc)

# 소문자로
abc = abc.lower()
print(abc)

# 입력한 문자열이 몇개 포함되어있는지 카운트
h_count = abc.count("h")
print(h_count)

# 문자열의 길이를 구하는 함수
length = len(abc)
print(length)

# 문자의 위치 찾기. 없으면 -1 반환
find = abc.find("o")
print(find)

# 인덱스. 찾고자 하는 문자가 없는 경우 error.
index = abc.index("o")
print(index)

# 공백 제거
ab = "   good  "
print(ab.strip() + "day") 
print(ab.lstrip() + "day")
print(ab.rstrip() + "day")

# 특정 문자로 나누기
profile = "김XX/30/대전/010-000-0000"
profile = profile.split("/")
print(profile)

```



### 튜플

- 리스트와 비슷한 자료형
- `( )` 소괄호 사용
- 튜플은 요소의 변경이 불가능하다(수정,상제,생성)

``` python
# example
tu = ()  # 튜블에 빈 값이 들어 있는 형태.
tu2 = (1,)  # 하나의 값이 있어도 반드시 ,를 넣어야 한다.
tu3 = 10, 20, 30, 40
tu4 = ("가", "나", ("ab", "cd"))

# 튜블 인덱싱, 슬라이싱, 연산
tu = ('a', 'b', 'c', 10, 1000)
print(tu[0])
print(tu[2:])

```



### Boolean

- 모든 자료형에 값이 있으면 True, 없으면 False
- `숫자 1` : True
- `숫자 0` : False
- `None` : False


``` python
# example code1
aa = 123
if(aa):
    print("True")
else:
    print("False")

# example code2
bb = None
if bb:
    print("True")
else:
    print("False")
```



### 리스트

- 다른 언어의 배열과 같음.

``` python
list_num = [10, 20, 30]
list_str = ["a", "b", "c"]
list_str2 = [10, 20,30, ["ab", "cd", "ef"]]
print(list_num)
print(list_str)
print(list_str2)

# 리스트 인덱식, 슬라이싱 (문자열과 같음)
list_str2[-1][-1]

# 3차원 리스트 example. '가' 가져오기
cc = [10, 20, ['aa', 'bb', 'cc', ["가", "나"]]]
cc_extract = cc[2][3][0]

# 인덱스 0 ~ 3까지 슬라이싱
ab = [1, 10, 100, 1000, 10000]
ab_slice = ab[:3]

# 인덱스 2 ~ 5까지 슬라이싱
bc = [1, 10, 100, ['aa', 'bb', 'cc'], 1000, 10000]
ab_slice = bc[2:5]

# 리스트 연산
aa = [10, 20, 30]
bb = [100, 200, 300]
print(aa+bb)  # 뒤로 연결됨
print(aa * 2)  # aa가 두번 연결됨
print(aa[0] * 2)  # 해당 값이 연산됨.

# 리스트 요소의 값은 변경 할 수 있음.
aa[1] = 100  

aa[2:] = ["가", "나"]

# 원는 구간에 새로울 리스트를 추가로 넣을 수 있음.
print(aa[1:3])
aa[1:3] = ["백", "천", "만"]

# 삭제
del aa[1:4]  # del 함수 사용(파이썬 내장함수)

aa[1:4] = []  # 빈 값 넣기

# 리스트 내에서 반복문을 통해 filter하기 example code
lists = [1,2,3,4,5,6,7]
filt = [i for i in lists if i % 2 == 0 ]

```



자주 사용하는 함수

``` python
# 뒤에 추가
li = [2, 1, 5, 4]
li.append(3)
print(li)

# 정렬
li.sort()
print(li)

# 순서 뒤집기
li.reverse()
print(li)

# 요소 위치 반환
index = li.index(3)
print("인덱스 :", index)

# 요소를 원하는 인덱스에 삽입
li.insert(2, 3)
print("리스트에 10을 insert", li)

# 원하는 값을 제거(첫 번째만 제거됨)
li.remove(3)
print(li)

# 리스트에서 요소를 꺼냄
print(li.pop()) # 가장 마지막 값 부터 꺼낸다.
print(li.pop(0)) # 원하는 index의 값을 꺼낸다

# 해당 값이 몇개 포함되어있는지 카운트
li_count = li.count(4)
print(li_count)

# 리스트 확장 함수 (append와 비슷)
a = [1, 2, 3]
a.extend([2, 3, 4, 5])
print(a)
```



### 딕셔너리(Dict)

- 사전, Map형태
- Key : Value 형.
- Key값으로 리스트 사용 불가능. 튜플 사용 가능.
 - ineex, key로 접근
- 한 항목을 item이라고 부름

```python
# example code

# 생성1 (빈 딕셔너리 생성)
dict0 = dict()

# 생성2
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = {"first": [1, 2, 3]}

print(dict1["key1"])
print(dict2["first"])


# item  추가
dict3 = {1: "안녕"}
dict3[2] = "하이"
dict3["인사"] = "굿모닝"


# for문을 이용해서 꺼내기
print(dict3)
for item in dict3.keys():
    print(item)


# item 삭제
del dict3[2]
print(dict3)


# 자주 사용하는 함수

# key 값을 value 얻기
dict3.get(1) # key가 없으면 None 을 반환
dict3[1] # key가 없으면 error


# item을 꺼내기. dict에서 제거된다.
dict3.pop(2)


# key 값이 없을 때 default 값을 줄 때
gender = dict3.get("gender", "default 값")


# value가 있는지 확인
"gender" in dict3


# value를 list로 반환
lue_list = dict3.values()

# Key와 value 한 쌍 얻기(items()). 튜플로 구성됨
dict3.items()


# key value 쌍을 모두 삭제
dict3.clear()
```


### 집합(set)

- 중복을 허용하지 않는다(중복을 제거할때 사용할수도있다)
- 순서가 없다

```python
# -*- coding:utf-8 -*-

set1 = set(['a', 'b', 'c'])
print(set1)

set2 = set([1, 2, 3])
print(set2)

# 출력해보니 원소 하나 하나를 넣어서 중복을 제거함
set3 = set("Hello World")
print(set3)

# 집합에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환해야한다.
set4 = set([1, 2, 3])
li = list(set4)


# 교집합, 합집찹, 차집합
set5 = set([1, 2, 3, 4, 5, 6, 7])
set6 = set([3, 6, 8, 9])

# 교집합 &
set_x = set5 & set6

# 합집합 |     둘 다 가능.
set5 | set6
set5.union(set6)

# 차집합 -     둘 다 가능.
set5 - set6
set5.difference(set6)

# 집합에 값 추가하기
set7 = set([1,2,3])
set7.add(100) # 하나의 값 추가 할 때
set7.update([10,20,30]) # 여러 개의 값을 추가 할 때

# 값 삭제하기
set7.remove(10) # 값이 없으면 error
set7.discard(10) # 값이 없어도 error가 발생하지 않는다.


# 대칭 차집합(^) : 두 개의 집합에서 한 쪽에만 존재하는 값들.
s = set("Good Morning")
t = set("Good Night")
print(s ^ t)
```





## 변수

- 의미를 부여하기 위해 만듬
- 객체를 가리키고 있다. (참조변수)

``` python
aa = 100
bb = 100
cc = 100
# 현재 reference count 가 3개다.

# is 함수(같은 값을 갖고 있는지 비교)
print(aa is bb)


# 변수 선언 및 초기화
c = d = 100 # 여러개의 변수에 동일 값을 대입 할 수 있다.
c, d = 100, 200
print(c, d)

(cc, dd) = ("aa", "bb")
print(cc, dd)

# 데이터를 복사하는데 있어서 혼동하기 쉬은 예
aa = ["a", "b", "c"]
bb = aa
aa[2] = "D"
print(bb) # 3번째 자리만 바뀐다.

# 슬라이싱을 하면서 다른 메모리에 저장해놓았기 때문에 값이 바뀌지 않는다.
aa = ["a", "b", "c"]
bb = aa[:]
aa[2] = "D"
print(bb)


# 변수의 scope
a = 20

def func(a):
    print("함수 내부", a)
    a = 10
    print(a)

func(a)


def func1(b):
    b = b+1
    print(b)

func1(30)


# Global 변수 선언
bb = 100
def bb_func():
    global bb # 함수 밖의 변수를 사용 하겠다는 뜻.
    bb += 1

bb_func()
print(bb)
```





## 비교 연산자 사용시 팁

``` python
# 비교 연산 &,| vs and,or
# and,or를 사용할 때 비교값이 False이면 
# 나머지 뒤의 연산을 하지 않음.
# 속도가 더 빠름.

# a와 10을 비교. False이기 때문에 else구문이 수행.
a = 0
if a and 10 / a:
    print('성공')
else:
	print('실패')


# a와 10을 비교. false이지만 나머지 두의 연산을 수행. ZeroDivisionError 생김
a = 0
if a & 10 / a:
    print('성공')
else:
	print('실패')
```





## def (함수, function)

``` python
""" 
def 함수(인수 ):
    내용
    return 값
"""


def show_max(a,b):
    if a > b:
        print(a,"는 최대값이다.")
    elif a == b:
        print(a, "와", b, "는 같다.")
    else:
        print(b, "는 최대값이다.")

show_max(10, 6)


# 여러개의 인자 전달. (인자가 튜플 형태로 된다)
def sum(*a):
    tot = 0
    for i in a:
        tot += i
    return tot

res = sum(10, 20, 30)
print(res)


# 튜플 형태로 return 하기
def return_var(a, b):
    return a+b, a-b

print(return_var(1,2))


# 인수에 초기값 설정
def show(name, age, gender="M"):
    print("이름 :", name)
    print("나이 :", age)
    if gender == "M":
        gender = "남자"
    else:
        gender = "여자"
    print("성별 :", gender)

show("HJ", 30)


# 키워드 인수. (인수의 순서와 상관없이 변수 이름으로 할당)
def show_info(name,age):
  print("이름:"+name+", 나이:"+age)

show_info(age=20, name="이름")


```

