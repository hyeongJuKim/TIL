# File

## 파일 읽기
사용자에게 파일명을 입력받아서 스크립트에서 파일을 열고 출력해 보겠다.

매개변수를 하나 받고 변수에 넣울 수 있는 값을 하나 반환한다.
```Python
# -*- coding: utf-8 -*-

from sys import argv

script, fileName  = argv

# 매개변수를 하나 받아서 파일 객체를 반환한다.
txt = open(fileName)

# txt에 있는 파일을 읽겠다.
print "파일 %r의 내용:" % (fileName)
print txt.read()
```

## 파일 읽고 쓰기
- `close`: 파일을 닫는다.
- `read`: 파일 내용을 읽는다. 결과를 변수에 담을 수 있다.
- `readline`: 텍스트 파일의 한 줄을 읽는다.
- `truncate`: 파일 내용을 비운다.
- `write(내용)`: 파일에 내용을 쓴다.

```Python
# 기본동작으로 읽기모드가 된다.
open("파일명")

# 두 번째 인자로 모드를 넣는다.
open("새 파일.txt", "모드")
```
open의 모드
- `r`: 읽기모드. 파일을 읽기만 할 때 사용.
- `w`: 쓰기모드. 파일에 내용을 쓸 때 사용.
- `a`: 추가모드. 파일의 마지막에 새로운 내용을 추가 시킬 때 사용.

