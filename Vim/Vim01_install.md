# Vim

## Vim?
Vim은 Vi와 호환되는 텍스트 에디터이다.  
Vim은 windows, Linux, MacOS 등 여러 환경에서 사용 가능하다. 

## Vim install
우선 vim을 설치합니다.
```
$ sudo apt-get install vim
``` 
설치가 완료되면 설정을 해봅시다.
```
$ vi ~/vimrc
```
처음에는 아무 내용도 없다.  
필요에 따라 아래 설정을 하면 됩니다.
```
set number            " line 표시를 해줍니다.
set ai                    " auto indent
set si                    " smart indent
set cindent            " c style indent
set shiftwidth=4      " shift를 4칸으로 ( >, >>, <, << 등의 명령어)
set tabstop=4         " tab을 4칸으로
set ignorecase      " 검색시 대소문자 구별하지않음
set hlsearch         " 검색시 하이라이트(색상 강조)
set expandtab       " tab 대신 띄어쓰기로
set background=dark  " 검정배경을 사용할 때, (이 색상에 맞춰 문법 하이라이트 색상이 달라집니다.)
set nocompatible   " 방향키로 이동가능
set fileencodings=utf-8,euc-kr    " 파일인코딩 형식 지정
set bs=indent,eol,start    " backspace 키 사용 가능
set history=1000    " 명령어에 대한 히스토리를 1000개까지
set ruler              " 상태표시줄에 커서의 위치 표시
set nobackup      " 백업파일을 만들지 않음
set title               " 제목을 표시
set showmatch    " 매칭되는 괄호를 보여줌
set nowrap         " 자동 줄바꿈 하지 않음
set wmnu           " tab 자동완성시 가능한 목록을 보여줌

syntax on        " 문법 하이라이트 킴"
```
 " 쌍따옴표는 주석을 의미한다
  
아래의 링크에서 단축키들을 볼 수 있습니다.  
[Vim단축키 정리](http://mintnlatte.tistory.com/170)