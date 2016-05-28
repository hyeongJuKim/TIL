# File

## 파일 읽기
사용자에게 파일명을 입력받아서 스크립트에서 파일을 열고 출력해 보겠다.

매개변수를 하나 받고 변수에 넣울 수 있는 값을 하나 반환한다.
```Python
# -*- coding: utf-8 -*-

from sys import argv

script, fileName  = argv

# 매개변수를 하나 받고 변수에 넣울 수 있는 값을 하나 반환한다.
txt = open(fileName)

# txt에 있는 파일을 읽겠다.
print "파일 %r의 내용:" % (fileName)
print txt.read()
```

