# -*- coding: utf-8 -*-

i = 0
numbers = []
j = 10



def numbers_status_print(i,j):
	while i < 6:
		print "꼭대기에서는 i %d" % i
		numbers.append(i)

		i = i + 1
		print "숫자는 이제: ", numbers
		print "바닥에서 i는 %d" % i




numbers_status_print(i,j)


print "숫자: "

for num in numbers:
	print num