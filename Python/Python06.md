# 40. 모듈, 클래스, 객체

#### 다른 파일의 모듈을 import 할 때
mystuff.py라는 모듈이 있다고 하자.  
```Python
# mystuff.py의 내용
def apple():
    print "나는 사과다!"

a = "난 그냥 변수다!"
```
이 모듈을 import해서 함수나 변수를 꺼내어 사용 할 수 있다.
```Python
import mystuff
mystuff.apple()
print mystuff.a
```
파이썬의 패턴
 - 키 = 값 형식으로 컨테이너를 쓴다. 
 - 키 이름으로 항목을 받아온다.  

### 모듈을 닮은 클래스
class 만들기  
```Python
class MyStuff(object):
    
    def __init__(self):
        self.a = "난 그냥 변수다!"

    def apple(self):
        print "나는 클래식 사과다!"
```
  
클래스는 인스턴스화를 해서 사용한다. 
```Python
thing = MyStuff()
thing.apple()
print thing.a
```

### 한 항목에서 다른 항목 받아 오기
```Python
# 사전 방식
mystuff['apples']

# 모듈 방식
mystuff.apples()
print mystuff.a

# 클래스 방식
thing = MyStuff()
thing.apples()
print thing.a

```
### 첫 클래스 예제
[ex40.py](ex/ex40.py)



