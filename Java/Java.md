# JAVA

[참초사이트 - 인프런](https://www.inflearn.com/course/자바java-언어-기본-강좌)

## 1. 기초

### 특징

- C++의 장점을 모아서 만듬
- C++의 문법과 구문 + Small talk의 객체지향
- 메모리 해제 -> Garbage Collertor
  - C에서는 `malloc()` , `free()`
  - C++에서는 `new`, `delete`
- 운영체제 상관없이 JVM 안에서 구동

| 운영체제                          |
| ----------------------------- |
| **JVM(Java Virtual Machine)** |
| **Java API(클래스 라이브러리)**       |
| **Java 언어**                   |



### 실행과정

- 확장자 `java`
- 전체 실행 과정
  - `*.java` -> `*.class` -> `JVM 실행`

### JVM과 JDK 설치

- JDK 구성
  -  Java 프로그램 개발 도구 (컴파일러 등)
  -  JRE -> JVM + 여러 표준 클래스
- www.oracle.com
  - JDK다운로드 -> JDK 설치


  

  

## 2.  자바 프로그램의 시작과 표준 출력

### 자바 프로그램 시작

```java
class ClassName {
  public static void main(String[] args){
    // code ..
  }
}
```

- JVM에서 메인들을 호출.

- `main(String[] args)` - 프로그램의 진입점

- `public` - 다른 곳에서도 호출 할 수 있도록.

- `static` - 클래스를 생성하지 않고도 호출 할 수 있다.

### 표준 출력

- java.lang 패키지

### Java 언어 키워드 (C, C++ 23개 + java 11개 = 44개) 

  

  

## 3. 데이터와 연산자

### 상수

- 사용하고 있는 모든 수, 불변의 값
- 숫자 상수
  - 정수형 상수
  - 부동소수점형 상수
- 문자 상수
  - 유니코드 - 'a', 'b' 등

``` java
// ex.
public static void main (String[] args){
  System.out.printf("%1$d %2$d", (int)'3',(int)'A');
}
```

### 데이터 형

- 기본형 - boolean, char, byte, short, int, long, float, double
- 참조형 - 메모리 주소를 저장하는 데이터형 (클래스, 배열, 인터페이스)
  - 4byte 크기

### 변수

- 상수를 저장하는 메모리 공간

### 연산자

- C언어와 동일 



## 반복문과 선택분

- 반복문

``` java
// for문 (java는 선언과 동시에 초기화 가능)
for (초기화; 조건식; 증감){
    // code
}

// while (true일 때 작동)
while(조건식){
    
}

// do ~ while
do{
    // 최초 한번 실행
} while (조건식){
    // code
}
```

- 선택문

```java
// if, else, else if
if (조건식){
    // code
} else if (조건식){
    // code
} else {
    // code
}

// case
switch(표현식){
  case 값1 : 
    // code
    break;
  case 값2 : 
    // code
    break;
  default :
    break;
}

// break - 반복문을 빠져 나온다.
// label - 반복문에 변수를 할당해서 브레이크 실행히 새당 반복문을 빠져나온다.
// continue - 하단 부분을 실행하지 않고 다음 반복문을 실행.
```



## 5. 배열

배열
- 같은 변수명 + 같은 데이터형 + 다수의 변수

``` java
// 배열 선헌 형식

// 1. 참조형 배열변수
int[] nArray;
int nArray[];

// 2. 객체.(크기를 확정)
nArray = new int[10];
```
이차원 배열

``` java
// 이차원 배열 선헌 형식

// 1.
int[][] nArray; // 타입[행갯수][열갯수]변수명
int nArray[][]; // 타입 변수명[행갯수][열갯수]

// 2.
nArray = new int[10][10]; //new 타입[행갯수][열갯수]
```



## 6. 클래스

### 형식

``` java
class 클래스명 {
    // field. comstructor
    // and method declarations
  
  
  void 메소드명(String str){
      
  }
   
}
```

### 객체 생성과 사용

`new 연산자 사용`

### 접근 제어자

| private       | 클래스 안에서만 접근 가능                 |
| ------------- | ------------------------------ |
| **public**    | **전체에서 접근 가능**                 |
| **protected** | **같은 클래스와 패키지, 하위 클래스에 접근 가능** |
| **friendly**  | **기본은 public**                 |

### 오버로딩

- 중복되는 메소드명을 클래스 안에서 정의 할수 있도록 하는 것
- 같은 함수명으로 다양한 값을 받아 처리
- 함수명 하나만 기억하면 된다  

### 생성자

- 객체가 생성될 떄 한 번 호출되는 메소드
- 자동으로 호출되는 메소드
- 리턴형이 없고 클래스명과 함수명이 같다
- public

### this, this()

- 객체  자신을 참조하는 참조형 클래스변수 또는 키워드
- `this.멤버변수` 
- `this.메소드()`

### static

### package, import

 



