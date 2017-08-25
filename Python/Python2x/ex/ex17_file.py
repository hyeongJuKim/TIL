# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "%s에서 %s로 복사합니다." % (from_file, to_file)

# 이 두 줄은 한 줄로도 쓸 수 있습니다. 어떻게 할까요?
indata = open(from_file).read()

print "입력 파일은 %d바이트입니다." % len(indata)

print "출력 파일이 존자하나요? %r"  % exists(to_file)
print "준비되었습니다. 계속하려면 리턴 키를, 취소하려면 CTRL-C를 누르세요."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "좋습니다. 모두 완료되었습니다."

# out_file.colse()
# in_file.close()