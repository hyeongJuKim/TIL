## if문

```python
"""
if 조건문1:
    print("명령1")
elif: 조건문2
    print("명령2")
else:
    print("명령")
"""
# and ,or , not
 
# in 연산자.
""" 문자열, 리스트, 튜블 안에 x가 존지하는지 확인.
ex)
x in 리스트
x not in 리스트
"""

num_list = [1, 2, 3, 4, 5]
print(3 in num_list)
print("나" in "가나다라")


# 중첩 if
aa = ["a", "b"]
flag = 1

if 'a' in aa:
    print("a를 가지고 있습니다.")
else:
    if flag:
        print("a를 가지고 있습니다")
    else:
        print("a를 가지고 있지 않습니다")
```



## for문

```python
""" for

for 변수 in 리스트
    실행문장
"""

# for문 기본
list1 = ['a', 'b', 'c']

for i in list1:
    print(i)


# example1
point = [90, 40, 30, 55, 100, 60]
number = 0

for i in point:
    number += 1
    if i >= 60: print("%d번 학생은 합격입니다. %d점" % (number, i))
    else: print("%d번 학생은 불합격입니다. %d점" % (number, i))
print(number)


# 튜플 예제
list_2 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for (i, j) in list_2:
    print(i + j)


# for문과 range 함수
"""
- range(1,5)  1,2번째는 자를 범위를 말한다.
- range(1,5,3) 세번째 숫자는 증가치를 뜻한다.
- 반복문에서의 else는 반복문이 다 끝난 후에 항상 수행한다.
  break 문을 사용했을 경우에는 수행되지 않는다.
"""

# example
for i in range(1, 5):
    if i % 2 == 0:
      break
    else:  
      print(i)
else:
    print("반복문 종료") # break문으로 빠져나오면 수행안됨.


# 구구단 출력 예제
for i in range(2,10):
    for j in range(2,10):
        print("%d * %d = %d" %(i,j,i*j), end=" ")
    print(" ")


# 리스트 안에 for문 사용하기
aa = [1,2,3,4,5,6,7,8,9]
gugudan_2 = []

# 방법1
for i in aa:
    gugudan_2.append(i*2)

print(gugudan_2)

# 2단을 리스트에 추가
gugudan_2 =[i*2 for i in aa]
print(gugudan_2)

# 5단중 짝수만 리스트에 추가
gugudan_2 =[i*5 for i in aa if i % 2 == 0]
print(gugudan_2)


# 구구단 결과를 저정하는 list
gugudan = [i*j for i in range(2,10)
               for j in range(2,10)]
print(gugudan)
```





## while문

```python
"""
while 조건문:
    실행문
"""
 
# example code
aa = 0
while aa < 10:
    aa += 1
    if 10 % aa == 0 : continue
    print("aa의 값:", aa)
    if aa == 10:
        print("종료합니다")

# break, continue도 Java와 같음
```





## generator

return 대신 yield라는 구문을 이용해서 함수 객체를 유지한 체 값을  호출자에게 넘겨준다.

 - 값을 넘겨준 후 함수 객체는 그대로 유지
  - 함수의 상태를 그대로 유지하고 다시 호출 할 수 있기 때문에 순회 가능한 객체를 만들 때 편리함.

``` python
# example code. 문자열 뒤집기.
def reverse(data):
  for index in range(len(data)-1, -1, -1):
    yield data[index]
    
for char in reverse('hello'):
  print(char)

```



