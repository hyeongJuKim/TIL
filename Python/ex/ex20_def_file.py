# -*- coding: utf-8 -*-

# sys모듈에서에서 argv를 가져온다.
from sys import argv

# 스크립트를 실행 할 때 받은 인자값을 unpack해서 각 변수에 할당한다.
script, input_file = argv

# 파일 전체를 출력하는 함수.
def print_all(f):
	print f.read()

# 파일의 헤드 위치를 이동한다.
def rewind(f):
	f.seek(0)

# 파일의line count와 한 줄을 읽고 헤드를 다음으로 넘긴다.
def print_a_line(line_count, f):
	print line_count, f.readline()

# 파일을 연다.
current_file = open(input_file)

print "파일 전체를 출력해 봅시다.\n"

print_all(current_file)

print "이번에는 테이프처럼 되감아 봅시다."

rewind(current_file)

print "세 줄을 출력해 봅시다."

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line +=  1
print_a_line(current_line, current_file)
