# Linux

## 리눅스로 개발 하는 모든 사람들이 꼭 봐야하는 동영상
[링크](http://luckyyowu.tistory.com/320)  

## Linux관련 검색이 필요한 것들 (검색 후 정리 필요)
- upstart
- systemd
- zsh
- ssh
- tmux
- scp
- cron
- rsyslog
- man 페이지

## 메모
- 참고사이트 [CentOS 명령어 정리](https://luna1x.wordpress.com/2013/10/06/centos--%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC/)  
- `apt-get`이 안될때는? a`pt-get update`  
- sudo가 없는 경우는 ? `apt-get install sudo`  


## 자주 쓰는 명령어

계정 권한 관리
```shell
useradd {계졍이름}      # 계정생성  
passwd {계정이름}       # 암호설정

su {계정이름}           # 계정 전환(계정 이름 입력하지 않으면 root 계정으로)

chown {변경할 소유자} {변경할 파일}
chdown -R {계정}:{계정} {directoryPath}     # root권한 폴더를 내 계정 폴더로 바꾸기
```

일반
```shell
history     # 사용햔 명령어들의 목록을 조회한다.
clear       # 콘솔창 clear

cp {fromFileName} {toFileName}	# 파일 복사.  
     -r	  # 하위 디렉토리까지 복사.
     -rp   # 파일의 소유자, 그룹자, 권한, 시간정보등 그대로 복사.  

rm          # 삭제
rm -r		# 하위 디렉토리, 파일까지 삭제
chmod {xxx} {file or Path}
```

디렉토리
```shell
ls      # 파일 목록을 간단히 출력한다.
ls -al  # 숨김일까지 포함해서 자세히 출력한다.
mkdir {direcotryName}       # 디렉토리를 생성한다.
mkdir -p dir3/dir2/dir1		# 필요하면 부모디렉토리까지 생성한다.
mv {원본} {이동할경로}      # 파일이동. (응용해서 파일명을 바꿀수 있다)
```

시스템 사용량 확인.
```shell
top     
top {옵션}

# 명령어 실행 후 사용 가능한 옵션
`Shift` + `m`     # 메모리 사용량이 큰 순서로 정렬.
`Shift` + `p`     # CPU 사용량이 큰 순서로 정렬.
`Shift` + `t`     # 실행시간이 큰 순서로 정렬.

# 원하는 프로세스만 보기
top | grep 'name'
```



## Bash vs zsh



## SUDO

sudo(super user do)