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