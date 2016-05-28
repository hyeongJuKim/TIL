# -*- coding: utf-8 -*-

from sys import argv

script, fileName  = argv

# 매개변수를 하나 받고 변수에 넣울 수 있는 값을 하나 반환한다.
txt = open(fileName)

# txt에 있는 파일을 읽겠다.
print "파일 %r의 내용:" % (fileName)
print txt.read()

print "파일 이름을 다시 입력해 주세요."
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
