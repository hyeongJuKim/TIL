# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
	print "황금으로 가득 찬 방입니다. 얼마나 가져갈까요?"

	next = raw_input(">")
	if "0" in next or "1" in next:
	 	how_much = int(next)
 	else:
 		dead("인간이여, 숫자 쓰는 법부터 배우도록.")

	if how_much < 50:
		print "좋아, 욕심부리지 않는군요. 당신이 이겼습니다!"
		exit(0)
	else:
		dead("욕심쟁이 얼간이 같으니!")



def bear_room():
	print "여기에는 곰이 한 마리 있습니다."
	print "곰은 꿀을 잔뜩 들고 있습니다."
	print "뚱뚱한 곰은 다른 쪽 문 앞에 있습니다."
	print "어떻게 곰을 움직이겠습니까?   (1.꿀 뺏기  2.곰 놀리기  3.문 열기)"
	bear_moved = False

	while True:
		next = raw_input(">")

		if next == "1": # 꿀 뺏기
			dead("곰이 당신을 쳐다보더니 목이 떨어져라 따귀를 날립니다.")
		elif next == "2" and not bear_moved: # 곰 놀리기
			print "곰이 문에서 비켰습니다. 이제 나갈 수 있습니다."
			bear_moved = True
		elif next == "2" and bear_moved: # 곰 놀리기
			dead("곰이 당신을 공격합니다.")
		elif next == "3" and bear_moved: # 문 열기
			gold_room()
		else:
			print "무슨 일인지 모르겠네요."


def cthulhu_room():
	print "여기는 대악마 크룰루를 봅니다."
	print "그분이, 그것이, 아니 뭐든지 간에 당신을 쳐다보고 당신은 미쳐갑니다."
	print "목숨을 위해 달아나려냐 네 머리를 먹어치우려냐?   (1.달아나기  2.먹기)"

	next = raw_input(">")

	if "1" in next: # 달아나기
		start()
	elif "2" in next: # 먹기
		dead("음, 맛이 좋군요!")
	else:
		cthulhu_room()


def dead(why):
	print why , "Game Over!!"
	exit(0)

def start():
	print "어두운 방에 있습니다."
	print "오른쪽과 왼쪽에는 문이 있습니다."
	print "어느 쪽을 고를까요?   (1.오른쪽  2.왼쪽)"

	next = raw_input(">")

	if next == "1": # 오른쪽
		bear_room()
	elif next == "2": # 왼쪽
		cthulhu_room()
	else:
		dead("문 주위에 맴돌기만 하다 굶어 죽었습니다.")


start()



