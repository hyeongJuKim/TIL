# 27. 논리 외우기

## 진리 용어
파이썬에서는 다음 용어를 써서 무엇이 'True'나 'False'인지 결정 한다.  
컴퓨터에서의 논리란 이 기호화 변수의 결합이 프로그램의 어떤 지점에서 True인지 보는 것이다.  

- and
- or
- not 
- != (같지 않다)  
- == (같다)  
- >= (크거나 같다)  
- >= (작거나 같다)  
- True  
- False  


## 진리표

**NOT**  
```
not False -> True  
not True -> False  
```
계
**OR**  
```
True or False -> True  
True or True -> True  
False or True -> True  
Flase or False -> False  
```

**AND**  
```
True or False -> False  
True or True -> True  
False or True -> False  
Flase or False -> False  
```

**NOT OR**  
```
not(True or False) -> False  
not(True or True) -> False  
not(False or True) -> False  
not(Flase or False) -> True  
```

**NOT AND**  
```
not(True or False) -> False  
not(True or True) -> False  
not(False or True) -> True  
not(Flase or False) -> True  
```

**!=**     
```
1 != 0 -> True  
1 != 1 -> False  
0 != 1 -> True  
0 != 0 -> False  
```
**==**   
```
1 == 0 -> False  
1 == 1 -> True    
0 == 1 -> True  
0 == 0 -> False  
```


# 28. 불린(boolean)연습
```Python

True and True
False and True
1==1 and 2==1
"test" == "test"
1==1 or 2!=1
True and 1==1
False and 0 != 0
True or 1==1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and not ("testing" == 1 or 1 == 0)
"chunky" == "bacon" and not (3 == 4 or 3 == 3)
3 != 4 and not (“testing” != “test” or “Python” == “Python”)
```

푸는법.  

1. 동등성(equality) 검사(==이나 !=)를 찾하서 해당 진리값으로 바꾼다.  
2. 괄호 안에 있는 and/or를 찾아 먼저 푼다.  
3. not을 찾아 뒤집는다.  
4. 남은 and/or를 찾아 푼다.   
5. 끝내면 True나 Flase가 나온다.  

# 29. if문 
### [ex29.py](ex/ex29_if.py)
이런 문법.  
```Python
if people < cats:
    print "고양이가 너무 많아요! 세상을 멸망합니다!"
```

# 30. else와 if
### [ex30_else_if.py](ex/ex30_else_if.py)
문법은 이렇다.
```Python
if cars > people:
    print "만약"
elif cars < people:
    print "또 만약"
else:
    print "나머지들.."
```

# 31. 결정하기
### [ex31.py](ex/ex1.py)
조건이 있는 스크립트를 만들어보자.  

- range 함수의 간단한 사용법.
```Python
a = range(10)

# 결과
[0,1,2,3,4,5,6,7,8,9]
```

- 숫자의 시작과 끝을 입력해서 숫자형 리스트를만든다.  
끝자리는 포함되지 않는다.
```Python
b = range(3, 10)

# 결과
[3,4,5,6,7,8,9]
```

- 어떤 숫자가 범위 사이에 있는 지 검사하려면?  
```Ptyhon
x in range(1,10)
```

# 32. 순환문과 리스트
### [ex32.py](ex/ex32.py)
Python에서 List 
```Python
hairs = ['갈색','은색','파란색']
weights = [1,2,3,4]
```


# 33. while문
### [ex33_while.py](ex/ex33_while.py)
Boolean 표현식이 True가 될 때 까지 코드 블록을 계속 실행한다.  

# 34. 리스트 원소 접근

**기수와 서수**  
- 우리가 사용하는 list는 기수를 사용한다.
    - 기수 : 수를 나타내는 데 기초가 되는 수. 10진법에서는 0부터 9까지의 정수가 있다. 0부터 시작.
    - 서수 : 사물의 순서를 나타내는 수. 1부터 시작.

list 인덱싱
```Python
a = ["고양이", "토끼", "오리", "병아리"]

a[0]    # a의 첫 번째 요소 읽기. 고양이
a[-1]   # a의 마지막 요소 읽기. 병아리
a[-2]   # a의 마지막에서 두번째 요소 읽기. 오리
```

# 35. 분기와 함수
### [ex35.py](ex/ex35.py)
예제를 보고 간단한 콘솔 게임을 만들었다.




