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


# 28 불린(boolean)연습
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
푸는법
1. 동등성(equality) 검사(==이나 !=)를 찾하서 해당 진리값으로 바꾼다.  
2. 괄호 안에 있는 and/or를 찾아 먼저 푼다.  
3. not을 찾아 뒤집는다.  
4. 남은 and/or를 찾아 푼다.  
5. 끄내면 True나 Flase가 나온다.  

## 실행결과

## 더 해보기

## 자주 묻는 질문

