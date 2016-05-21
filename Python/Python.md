# Python

## Python의 기초
Python 파일명은 끝에 `.py`가 되어야 한다.  
Python을 실행할때는 commandLine에 `python` 이라고 입력한다.  
Python을 종료할때는 `exit()` 이라고 입력한다.
  
파일에 한글내용을 쓰려면 스크립트 가장 위에 이렇게 적자.
```Python 
#-*-coding: utf-8-*-
```

## Python 첫 번째 프로그램

프린트하기 `ex01.py`
``` Python
print "text"
print 'text2'
print "t'e'xt3"
print 't"e"xt4'
```
  
주석처리하기 `ex02.py`
``` Python
# 이렇게하면 한줄주석
print "여긴 문자가 출력된다 ! "

"""
이렇게 하면
여러 줄을 주석 처리 할 수 있다.
"""
```
수와 계산 `ex03.py`
``` Python
+ 덧셈(plus)
- 뺄셈(minus)
* 곱셈(slash)
/ 나눗셈(asterisk)
% 나머지(percent)    # 연산자와 피연산자를 나누고 난 나머지 값.
< 작다(less than)
> 크다(greater than)
<= 작거나 같다(less than equal)
>= 크거나 같다(greater than equal)
```

변수와 이름 `ex04.py`
```Python
{변수명} = {값}  # 이렇게 값을 원하는 변수명에 할당하여 사용할 수 있다.
```

변수와 출력 `ex05.py`
``` Python
%s  # 문자열
%d  # 정수
%c  # 문자 한개
%f  # 부동소수
%o  # 8진수
%x  # 16진수

# 예제
# 한개일 때
print "$s하네" $"신기"

# 여러개 일 때
y = "%s과 %s이다 %s 사람." %("사랑","전쟁")

```

문자열과 텍스트





