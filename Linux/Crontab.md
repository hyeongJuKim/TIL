# Linux

## crontab?
- 리눅스의 스케쥴을 관리하는 명령어.
- 특정 시간에 스크립트나 명령어가 수행되도록 등록.
- /etc/rc.d/init.d/crond스크립트에 의해 시작, 종료, 재시작될 수 있습니다.
- 로그 에 변경,수행 이력이 기록됨. ( /varlog/cron/ )
  
## 참고사이트
[제타위키](http://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%B0%98%EB%B3%B5_%EC%98%88%EC%95%BD%EC%9E%91%EC%97%85_cron,_crond,_crontab#.EC.B0.B8.EA.B3.A0_.EC.9E.90.EB.A3.8C)  
[JDM's Blog : 크론탭 사용법](http://jdm.kr/blog/2)  
[리눅스 포털 : 주기적이고 반복적인 cron 설정작업 활용 1편](https://www.linux.co.kr/home2/board/subbs/board.php?bo_table=lecture&wr_id=1246) 

## crond (크롬데몬)
시스템에서 cron이 동작하려면 crond라는 크롬 데몬이 동작하고 있어야한다.
잘 돌아가나 확인 해보자
```
$ ps -ef |grep crond
```
    
crond 실행, 중지 재시작  
- /etc/rc/d/init.d/crond 스크립트를 이용한다.

`crond start` 시작  
`crond restart` 재시작  
`crond stop` 종료  


## crontab 기본
- `crontab -e` 크론탭 열기.  
- `crontab -l` 크론탭 리스트 보기.  
- `crontab -d` 크론탭 리스트 보기.  

## 주기설정
\*     \*      \*      \*      \*  
분(0-59) 시간(0-23) 일(1-31) 월(1-12) 요일(0-7)
  
  
매분 실쟁
```
#test.sh
*****/home.script.test.sh
```
  
특정 시간 실행
```
# 매주 토요일 오후 2시 5분에 test.sh를 실행
5,14,** 6/home.script.test.sh
```
  
  
반복 실행
```
# 매일 매시간 0분, 20분, 40분에 test.sh 를 실행
0,20,40 **** /home/script/test.sh
```


