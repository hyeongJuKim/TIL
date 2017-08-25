# -*- coding: utf-8 -*-

"""
프롬포트와 사용자.
ex11처럼 입력값을 받아 출력을 할 수 있지만,
이번 예제 처럼 더 간단하게 사용 할 수 있다.
"""

age = raw_input("몇 살이죠? ")
height = raw_input("키는 얼마죠? ")
weight = raw_input("몸무게는 얼마죠? ")

print "네, 나이는 %r살, 키는 %r, 몸무게는 %r이네요" %(
	age,height,weight
)
print "뜬금없지만, 태양의 각 지름은 %r입니다." % '''32'10"'''
