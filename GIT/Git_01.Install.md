# Git

## 기본용어
**커맨드라인(Commind Line):** 맥의 터미날과 유사.

**저장소(Repository):** 프로젝트를 저장하는 공간(디렉토리). 줄여서 'repo'라고도 부름

**버젼관리(Version Control):** 

**커밋(Commit):**

**브랜치(Branch):**

## 자주쓰는 명령어
`git help config` : 도움말.  
`git init` : 디렉토리를 로컬저장소로 초기화한다.  
`git --global core.editor` : 어떤 편집기를 사용할지 설정한다.  
`git confing --list` : 설정한 정보들을 보여준다.  
`git config {key}` : key에 대한 값을 확인 할 수 있다.  
`git status`  : 상태 확인하기  
`git status -s`  : 간단하게 상태 확인하기  
`git diff` : 수정했지만 아직 staged상태가 아닌 파일을 비교한다.  
`git remote` : 리모트 저장소 확인하기.  

## git 가이드
> GIT을 사용해보고 간단하게 정리.

## git이란?  
> 프로그램의 소스코드 관리를 위한 **분산관리시스템**이며, 빠른 수행 속도가 장점이다.  
최초에는 리누스 토르발스가 리눅스 커널 개발에 이용하려고 개발하였으며, 현재는 다른 곳에도 널리 사용되고 있다.  
> 깃의 작업 폴더는 모두, 전체 기록과 각 기록을 추적할 수 있는 정보를 포함하고 있으며, 완전한 형태의 저장소이다.  
> 네트워크에 접근하거나 중앙 서버에 의존하지 않는다.  

## Git파일의 세 가지 상태
Git파일은 Committed, Modified, Staged의 세 가지 상태로 관리한다.  

- Committed : 데이터가 로켈 데이터베이스에 안전하게 저장됬다는것을 말한다.
- Modified : 수정한 파일을 아직 로컬 데이터베이스에 커밋하지 않은 것을 말한다.
- Staged :  현재 수정한 파일을 곧 커밋할 것이라고 표시한 상태를 의미한다.

## Git프로젝트의 세 가지 단계
- Git directory(repository) : Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳.
- Working directory : 프로젝트의 특정 버전을 CheckOut한것이다.  
- Staging area : Git 디렉토리에 있다.  단순한 파일이고 곧 커밋할 파일에 대한 정보를 저장한다.

## Git 설치

### 1.리눅스에서 설치
```
$ sudo yum install git-core
```
또는
```
$ sudo apt-get ins tall git
```

### 2.Mac에서 설치
[https://git-scm.com/downloads](https://git-scm.com/downloads)에서 설치

## Git 최초 설정
### 로컬 저장소 만들기
사용할 프로젝트 폴더를 만든 후 그 안에서 `git init`을 타이핑한다.  
`touch Readme.md`로 파일 생성.  

### 사용자 정보
사용자 이름과 이메일 주소를 설정한다. Git은 커밋할 때마다 이 정보를 사용한다. 한 번 커밋한 후에는 정보를 변경할 수 없다.
```
$ git config --global user.name "HJ Kim"
$ git config --global user.email "gudwndhkd@nate.com"
```
프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 `--global` 옵션을 빼고 명령을 실행한다.  
`git config --list` 명령을 실행하면 설정한 모든것을 보여준다.


## 회원가입
[https://github.com](https://github.com) 에서 회원가입 후 로그인 한다.

---

## Git 저장소 만들기

### 로컬에 저장소 만들기
원하는 위치에 디렉토리를 생성해서 해당 디렉토리로 이동 후 `git init`으로 저장소를 만든다.
```
$ mkdir ~/{ProjectName}
$ cd ~/{ProjectName}
$ git init
$ touch readme.md
```

다음 코드를 입력해 보자.
```
git status
```
  
이런 텍스트가 나올것이다.
```
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    readme.md

nothing added to commit but untracked files present (use "git add" to track)
```

## 저장소 생성
오른쪽 상단의 플러스 아이콘을 누른 후 New repository를 선택해서 자장소를 생성한다.

## 저장소 복제

git에 있는 저장소를 복사 할 때.
```
$ git clone {url}
```
또는 
```
$ git clone {url} {newFolderName}
```

## 저장소에 저장하기

파일을 추가 후 `git status`를 입력해보자.
```
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    GIT/

nothing added to commit but untracked files present (use "git add" to track)
```
이것은 아직 Untracked 상태에 있다는 것이다.  
아래의 코드를 입력해서 Tracked 상태로 바꿔보자.  
```
$ git add {fileName or folderName}
```
다시 한번 `git status`를 입력해보자.
```
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   GIT/Git.md

```

"Untracked files"부분에서 "Changes to be committed"로 바뀐 것을 볼 수 있다.  
커밋을 하면 `git add`를 실행한 시점의 파일이 커밋되어 자장소 히스토리에 남는다.  

**파일 무시하기** : GIT관리를 무시하려면 `.gitignore` 파일을 만든 후 그 안에 추가하자.  

`git diff` : Staged와 Unstaged 상태의 변경 내용 비교하기  
`git diff --cached` : staged 사태인 파일 확인하기

## 변경하상 커밋하기
`git status`로 상태를 확인 후 커밋하자.
```
$ git commit -m "connents"
```

## 파일 삭제하기

## 파일 이름 변경하기

## Remote 저장소
인터넷이나 네트워크에 존재하는 저장소.  

`git remote` : 리모트 저장소 확인하기.  
`git remote -v` : 리모트 저장소 확인하기.(URL)  
`git remote rename {변경할 이름} {변경될 이름}` : 리모트 저장소 이름 변경.  
`git remote mv {변경할 이름} {변경될 이름}` : 디렉토리 변경.  
`git remote rm {remoteName}` : 리모트 저장소 삭제.  

## 커밋 후 remote저장소에 push하기
커밋이 완료되면 push를 해보자.
```
$ git push
```
또는
```
$ git push {RemoteRepoName} master
```




## 사용자 정보 설정 
 `command` + `,`키를 누른 후 fullName 과 Email Address를 설정하면 모든 저장소에 설정이 된다. 
    $ git config --global user.name {HJ}
    $ git config --global user.email {gudwndhkd@nate.com}
                --global을 생략하면 현재 저장소에만 적용된다.

