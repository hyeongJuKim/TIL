## r, w, a, b 모드 및 tempFile 모듈

``` python
# 임시로 파일을 만들어서 돌려주는 함수. (중복되지 않도록 만들어줌)
tempfile.mktemp() 

# 임시적인 저장공간으로 사용될 파일 객체를 돌려주는 함수. (w+b모드)
tempfile.TemporaryFile()
```



모드

- w 쓰기 모드로 파일 열기
  - 파일이 없으면 새로 생성.
  - 파일의 시작에 포인터가 위치
- w+ 읽기와 쓰기 모드로 연다. (파일이 없으면 새로 생성)
- r  읽기 모드로 파일 열기
  - 파일의 시작에 포인터가 위치
- a  추가모드로 파일 열기
  - 쓰기모드로 파일을 연다 (파일이 없으면 새로 생성)
  - 파일의 끝에 포인터가 위치
- a+ 읽기, 쓰기모드로 파일을 연다. (파일이 없으면 새로 생성)
  - 파일의 끝에 포인터가 위치 
- b  바이너리 모드로 파일 열기
  - b는  단독사용 X. w,r,a (뒤에 붙여서 사용)

