# Java의 정석
## Chapter 5 배열(Array)
### 1. 배열(Array)
#### 1.1 배열(Array)이란?
같은 타입의 여러 변수를 하나의 묶음으로 다룬 것.
```java
// 5개의 int 값을 저장할 수 있는 배열을 생성한다.
int[] score = new int[5] 
```
#### 1.3 배열의 생성
```java
// 참조변수 선언. 데이터를 저장할 수 있는 공간은 아직 마련되지 않음.
int[] score; 

// 5개의 int값을 자장 할 수 있는 공간 생성.
score = new int[5]; 
```

#### 1.6 다차원 배열

#### 1.8 배열의 복사
```java
int[] number = {1,2,3,4,5};
int[] newNumber = new int[10];

for(int i = 0; i <number.length; i++){
	//배열 number의 값을 newNumber에 저장한다.
	newNumber[i] = number[i]; 
}

```
