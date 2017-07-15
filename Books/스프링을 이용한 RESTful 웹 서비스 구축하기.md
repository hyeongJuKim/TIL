# 스프링을 이용한 RESTful 웹 서비스 구축하기

## 차례
### 01 들어가기
#### 1.1 개요
#### 1.2 REST
REST의 제약 조건들.  
- 클라이언트/서버 : 웹의 일괄된 인터페이스를 따른다는 전제하에 클라이언트와 서버는 독립적으로 구현되어야 한다. 
- 균일한 인터페이스 : 자원 식별, 표현을 통한 자원 처리, 자기 서술적 메시지, HATEOAS같은 인터페이스 제약에 따라 서로 일관성 있게 상호 운영되어야 한다.
- 계층 시스템 : 웹의 일관된 인터페이스를 사용해서 프락시 또는 게이트웨이같은 네트워크 기반의 중간매체를 사용할 수 있어야 한다.
- 캣; 찰; : 웹 서버가 응답 데이터마다 캐시 여부를 선얼할 수 있어야 한다.
- 무상태 : 웹 서버가 클라이언트의 상태를 꽌리할 필요가 없어야 한다.
- 주문형 코드 : 선택사항으로 스크립트나 플러그인 같은 실행 가능한 프로그램을 클라이언트에 전송하여 클라이언트가 실행할 수 있도록 해야 한다.

REST API에서의 CRUD
URL에 나타내지 않는다.

| HTTP Method | 의미                | CRUD   | 예제              |
| ----------- | ----------------- | ------ | --------------- |
| POST        | 새로운 자원을 생성        | Create | POST /Books     |
| GET         | 재원을 조회            | Read   | GET /Books/1    |
| PUT         | 기존에 존재하는 자원을 변경   | Update | PUT /Books/1    |
| DELETE      | 기존에 존재하는 자원을 삭제한다 | Delete | DELETE /Books/1 |

### 02 Spring 3.2와 REST
도서 정보를 처리하는 REST API 서비스를 만든다.  
조회, 등록, 수정, 삭제기능 구현한다.  
#### 2.1 요구사항 정의
- 도서 정보 목록을 조회할 수 있어야 한다.
- 도서 상세 정보를 조회 할 수 있어야 한다.
- 도서 정보를 등록할 수 있어야 한다.
- 도서 정보를 수정할 수 있어야 한다.
- 도서 정보를 삭제할 수 있어야 한다.
#### 2.2 개발환경
- Java 6 이상
- Meven 3.0.x
- LogBack / SLF4j
- Spring 3.2
- MyBatis 3.2
#### 2.3 개발 환경 구축하기
- Maven Project생성
  - Meven 설치
``` shell
# Maven Project 생성.
mvn archetype:generate

# Maven Project 생성(옵션 추가)
# groupID: 프로젝트가 속하는 그룹 식별값. 패키지 형식으로 표현한다.
# artifactId: 프로젝트 결과물의 식별값. 프로젝트나 모듈을 뜻한다.
mvn archetype:generate -DgroupId={com.mycompany.app} -DartifactId={my-app} -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=falseclear

# 소스코드 컴파일하기. (target/classes 디렉토리에 생성됨)
mvn compile

# 테스트 클래스 실행하기 (성공여부 출력됨)
# 컴파일된 테스트 클래스들target/test-classes 디렉토리에 생성됨.
# 테스트 결과 리포트는 target/surefire-reports 디렉토리에 저장된다.
mvn test

# 배포 (war파일,jar파일 생성)
mvn package
```

- github에 저장,(README.md파일 생성, .gitignore파일 생성)
- pom.xml 설정
- 로그 설정하기 
  - `src/main/resources/logback.xml`
  - LogLevel
- servlet 설정하기 `web.xml`
- `AppConfig.java` , `RestConfig.java`

### 03 Persistence Layer
- DataBase

  - DataBase 생성, Table생성
  - User 생성, 권한.
  - DataBase  연결
  - Model Class 구현.
  - Mapper 구현.
  - Mapper Interface
  - Junit으로 테스트코드 작성.


### 04 Business Layer

- 트랙잭션 관리
  - AppConfig 설정 파일에 트랜잭션 관리자 추가
  - 전파 규칙, 격리 수준
- Service 구현
  - Service (InterFace)
  - ServiceImpl
    - @Service, @Transaction 추가
  - service Test

### 05 Presentation Layer
- HttpMessageConverter를 이용한 Controller 만들기.  
- URL Tamplate (@PathVariable. URL경로에 있는 변수 사용하기)
```java
@Requestmapping(value = "/{id}", method = RequestMethod.GET)
@ResponseBody
public Book getBook(@PathVariable("id") Long id){
  Book book = bookService.getBook(id);
  return book;
}
```
- Controller 구현
- RestAppConfig 설정 파일에 Controller 추가하기
- JSON
- XML
- ControllerNegtiation
- HTTP Method Conversion
  - 스프링의 HiddenHttpMethodFilter클래스 사용
    - httpMethodFilter을 web.xml에 등록. 
- 예외처리

