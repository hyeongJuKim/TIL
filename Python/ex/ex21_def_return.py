# -*- coding: utf-8 -*-

# 반환하는 함수를 만들어 보자


def add(a, b):
	print "덧셈 %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "뺄셈 %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "곱셈 %d * %d" % (a, b)
	return a * b

def devide(a, b):
	print "나눗셈 %d / %d" % (a, b)
	return a / b


print "함수만으로 계산해 봅시다."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "나이: %d, 키: %d, 몸무게: %d, IQ: %d" % (age, height, weight, iq)

# 추가 점수 문제
print "문제가 있어요"

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))
print "결과:", what, "손으로 계산 할 수 있나요?"
