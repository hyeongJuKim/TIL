# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "잠깐 아직 목록에 10개가 들어 있지 않으니 한 번 고쳐 봅시다."

stuff = ten_things.split(' ')
more_stuff = ['Day','Night','Song','Frisbee','Corn','Banana','Gril','Boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "추가" , next_one
	stuff.append(next_one)
	print "이제 %d 항목이 있습니다." % len(stuff)

print "한 번 볼까요!", stuff

print "이걸로 무언가 해봅시다."

print stuff[1]
print stuff[-1] # 으아 복잡해
print stuff.pop()
print ' '.join(stuff) #  ' '으로 리스트를 join한다.
print '#'.join(stuff[3:5]) # 리스트의 3부터 4까지 #으로 join한다.range(3,5)와 비슷.
