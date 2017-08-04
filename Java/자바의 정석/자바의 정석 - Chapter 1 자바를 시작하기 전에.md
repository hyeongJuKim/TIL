# Java의 정석

## Chapter 1 자바를 시작하기 전에

### 1. Java(Java Programming Language)
#### 1.3 자바언어의 특징
- 운영체제에 독립적
- 객체지향언어 - 상속, 캡슐화, 다형성
- 자동 메모리 관리(Garbage Collection)
- 네트워크와 분산처리 지원
- 멀티쓰레드 지원
- Dyanamic Loading 지원 - 일부클래스가 변경되어도 전체 어플리케이션을 다시 컴파일 하지않아도 됨.

#### 1.4 JVM(Java Virtual Machine
- Java를 실행하기 위한 가상 머신.

### 2. 자바개발환경 구축하기

### 2.1 자바 개발도구(JDK) 설치
- Java Development Kit
- JDK의 bin디렉토리에 있는 주요 실행 파일들
  - javac - 자바 컴파일러, 자바소스코드를 바이트코드로 컴파일한다.
    `javac Hello.java`
  - java - 자바 인터프리터, 컴파일러가 생성한 바이트코드를 해석하고 실행한다.
    `java Hello.java`
  - javap - 역어셈블러, 컴파일된 클래스 파일을 원래의 소스로 변환한다.
    `javap Hello.java`
  - appletviewer - 애플릿 뷰어, HTML문서에 삽입되어 있는 애플릿을 실행시킨다.
    `appletviewer Hello.html`
  - javadoc - 자동문서생성기, 소스 파일ㄹ에 있는 주석을 이용하여 Java API 문서와 같은형식의 문서를 자동으로 생성한다.
    `javadoc Hello.java`
  - Jar - 압축 프로그램, 클래스파읽과 프로그램의 실행에 관련된 파일을 하나의 jar파을로 압축하거나 압축 해제한다.
    압축할 때 `jar cvf Jello.jar Hello1.class Hello2.class`
    압출 풀 때 `jar xvf Hello.jar`

### 3. 자바 프로그램 장석하기
#### 3.1 Hello.java
올바른 작석 예

```java
/* Hello2.java */
public class Hello2()
  	   class Hello3()
/* public class가 있는 경우, 소스파일의 이름은 반드시 public class의 이름과 일치해야 한다. */
```
```java
/* Hello2.java */
class Hello2()
class Hello3()
/* public class가 하나도 없는 경우, 소스파일의 이름은 'Hello2.java', 'Hello3.java' 둘 다 가능하다. */
```

