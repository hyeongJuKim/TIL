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

변수와 출력, 문자열 `ex05.py`,`ex06.py`,`ex07.py` `ex08.py`
``` Python
%s  # 문자열
%d  # 정수
%c  # 문자 한개
%f  # 부동소수
%o  # 8진수
%x  # 16진수

%r  # 변수에 있는 자료를 그대로(raw data) 보여준다.
```
한개일 때
```Python
print "%s과 공포이다." "충격"
# 결과 ->  충격과 공포이다
```
여러 개 일 때
```Python
# 여러개 일 때 %() 괄호 안에 변수를 넣는다.
print "%s과 %s이다." %("충격","공포")
# 결과 -> 충격과 '공포'이다
```
문자열을 이렇게 곱할 수도 있다.
```Python
print "*" * 10 
# 결과 -> **********
```
문자열 더하기.  
- +로 연결 : 공백 없이 연결된다.  
- 쉼표(,)로 연결 : 공백이 생기면서 연결된다. 다음 라인을 연결 할 수 있다. 
```Python
print "맛" + "있" + "는" ,
print "치" + "즈" + "버" + "거"
# 결과 -> 맛있는 치즈버거
```
문자열 한 줄 이상 출력하기
```Python
print """
여기에 문자를 입력하면
한 줄 이상 출력 가능하게 된다.
"""
```

\ (역슬래시) 문자로 여러가지 문자를 입력 할 수 있다.  
```Python
print """
\\  역슬래쉬  
\'  작은 따옴표  
\"  큰 따옴표  
\a  ASCII 벨소리(BEL)
\b  ASCII 벨스페이스(BS)
\F  ASCII 폼 피드(formfeed) (FF)
\n  줄바꿈
\t  수평 탭
\v  수직 탭
\ooo 8진수 값 oo에 해당하는 문자
\xhh 16진수 값 hh에 해당하는 문자
"""
```
Python 입력받기
```Python
raw_input("이 곳에 Prompt를 넣는다.")
```