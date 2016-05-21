# Docker

## 목차

## 참고 사이트

[docker Install](http://blog.nacyot.com/articles/2014-01-27-easy-deploy-with-docker/) <br>
[docker cheatSheet](https://gist.github.com/nacyot/8366310)

## 용어 정리
#### 이미지

서비스 운영에 필요한 서버 프로그램, 소스코드, 컴파일된 실행파일을 묶은 형태. <br>
저장소에서 올리고 받는다 (push, pull)

#### 컨테이너

이미지를 실행한 상태. <br>
이미지 하나로 여러개의 컨테이너를 만들 수 있다.

#### Docker의 이미지 처리 방식

Docker는 베이스 이미지에서 바뀐 부분만 이미지로 생성한다. <br>
컨테이너로 실행 할 때에는 베이스 이미지와 바뀐 부분을 합쳐서 실행한다. <br>
각 이미지는 의존관계가 형성된다. <br>

## 자주쓰는 docker 명령어 모음

- pull명령으로 이미지 받기

``` 
docker pull {이미지이름:태그}
```

- docker 이미지 보기
``` 
docker images   //모든 이미지의 정보 보기
docker images {이미지명}   //해당 이미지 정보만 보기
```

- docker 이미지 run
```
docker run -itd {컨테이너명}    // 컨테이너 run
docker rm {이미지명}   // 컨테이너 삭제
```

- 컨테이너 목록 보기
```
docker ps   // 현재 실행중인 docker만 보여줌
docker ps -a    // 모든 docekr를 보여줌
```

- 컨테이너 생성, 실행
```
docker run -itd {이미지명} --name {생성할 컨테이너명}
```

- 컨테이너 시작/종료
```
docker start {컨테이너명}        // 컨테이너 시작
docker restart {컨테이너명}      // 컨테이너 재시작
docker stop {컨테이너명}         // 컨테이너 정지
docker attach {컨테이너명}       // 실행중인 컨테이너에 접속하기

ex) 컨테이너를 다시 run, 컨테이너로 접속, 아파치 올리기 , 빠져나오기
     docker start {컨테이너명}
     docker attach {컨테이너명}
     service apache2 start
     Control + P , Contorl  + Q 로 빠져나오기
```

- 컨테이너 올리기 (Apache)
```
docker run -itd —name {컨테이너명} -p {port}{port} {이미지명} bash
docker run -itd -v /hjWorld:/var/www/html --name hjWorld -p 80:80 php:5.5-apache bash
추가옵션 :   —link {Names}:Alias

PHP log 보기
tail -f /var/log/apache2/*
```

- 컨테이너 올리기 (MySQL)  
[참고사이트](http://blog.naver.com/PsssostView.nhn?blogId=alice_k106&logNo=220347048673)
```
docker run -d --name mysqltest -p (열려있는 포트):3306 -e MYSQL_ROOT_PASSWORD=(원하는 PWD) mysql
```
- MySQL 접속 DB생성

```
// mySql 컨테이너 접속
docker exec -i -t mysqltest bash

// mySql 접속
mysql -u root -p

// DB만들고 확인
create database {database 이름};
show databases;
```    












