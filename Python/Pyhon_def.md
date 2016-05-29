# 이름, 변수, 코드, 함수

## 함수 만들어보기
define라는 뜻 def로 만들 수 있다.
```Python

# 필요한 인자들을 받아서 함수 내에서 사용한다. (인자를 받아서 unpack한다)
def print_two(*args):
    arg1, arg2 = args
    print "실행인자1: %r, 실향인자2: %r" % (arg1, arg2)

# 필요한 인자들을 받아서 함수 내에서 사용한다.
def print_two_again(arg1, arg2):
    print "실행인자:1 %r, 실행인자2: %r" %(arg1, arg2)

# 인자를 하나만 받는다.
def print_one(arg1):
    print "실행인자1: %r" % arg1

# 인자를 받지 않고 실행한다.
def prnit_none():
    print "아무것도 받지 않음."

print_two("Hi","HJ")
print_two_again("Hi","HJ")
print_one("First!")
prnit_none()

```

## 함수와 변수
