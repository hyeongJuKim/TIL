# Python3 - 00. Python언어

Python3를 공부하면서 잘 몰랐던거나  헷갈리는것 중에 카테고리를 찾지 못한 경우 여기에 정리



## \__name__

Python 내부적으로 사용하는 변수이다.

파이썬 인터프리터는 소스파일을 읽으면서 해당 파일의 모든 코드를 실행한다.

직접 파일을 실행 할 경우 \_\_name\_\_ 변수에 '\_\_main\_\_' 이라는 값을 저장하고,

다른 파이썬 모듈에서 import해서 사용 할 경우에는  \_\_name\_\_ 변수에 {사용한 모듈 파일명}이 저장된다.

``` python
if __name__ =='__main__':
    print('직접 실행됨')
else:
    print('import되어 실행됨')
```





## 파라미터 종류



``` python
# *args 튜플 형태.
def print_args(*args):
    print(args)
    for i in args:
        print(i)

print_args(1, 2, 3)


# **kwargs 딕셔너리 형태.
def print_kargs(**kwargs):
    for k, v in kwargs.items():
        print("Key : ", k)
        print("Value : ", v)

print_kargs(name="yasoob", age=30)

```