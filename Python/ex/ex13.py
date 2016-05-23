# -*- coding: utf-8 -*-

# 매개변수, 풀기(unpack), 변수

# import: python에서 필요한 모듈을 가져다 씀.
from sys import argv

# 스크립트를 실행 할 때 전달했던 실행인자가 담겨 있다.
# 이것을 풀어서 순서대로 변수에 대입한다.
script , first, second, thrid = argv

print "스크립트 이름:", script
print"첫 번째 변수", first
print"두 번째 변수", second
print"세 번째 변수", thrid

