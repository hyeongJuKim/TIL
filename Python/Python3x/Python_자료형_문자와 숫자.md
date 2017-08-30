### 숫자형


```python
""" 숫자
 (사칙연산은 다른 java와 똑같음)
 a ** b : a의 b승
 % : 나머지 값을 반환.
 // : 소수점 자리를 버리는 연산자.
"""
num_a = 10
num_b = 10

print(num_a + num_b)
print(num_a ** num_b)

print(5 % 2)

print(3/2)
print(3//2)
```



### 문자열

```python

""" 문자열
 char형이 따로 없다.
 이스케이프 코드
    \n : 줄바꿈
    \r : 캐리지 리턴. 줄바꿈 후 커서를 바뀐 줄로 위치시킨다.
    \000 : null 문자
    \t : 수평 탭
    \" : 큰따온표 출력
"""

# 문자열 종류
str_a = "큰 따온표."
str_b = '작은 따온표.'
str_c = """큰 따온표 3개.
줄 바꿈도 인식한다."""

print("str_a:", str_a)
print("str_b", str_b)
print("str_c", str_c)


# 문자열 더하기
str_concat1 = "Hello"
str_concat2 = " World"
print(str_concat1 + str_concat2)


# 문자열 곱하기
print("Hello" * 3)


# 문자열에도 인데스가 있다.(음수는 뒤에서부터)
str = "20170831010230"
print(str[0] + str[1] + str[2] + str[3])
print(str[-4] + str[-3] + str[-2] + str[-1])


# 문자열 슬라이스
print(str[3:8])  # 원하는 구간을 슬라이스
print(str[:8])  # 시작 생략 가능
print(str[8:])  # 끝 생략 가능
print(str[:])  # 전부 출력


# 문자열 교체.  문자열 튜플 자료형은 그 요소값을 변경할 수 없다.
str1 = "ABCD"
print(str1[1])

# str[1] = "F"
# print(str1)  # ERROR

print(str1[:1] + 'F' + str1[2:])


# 문자열 format : 문자열 내에 어떤 특정 값을 변경.
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
