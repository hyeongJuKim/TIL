# -*- coding: utf-8 -*-

class Song(object):
	
	# 클래스를 초기화?
	def __init__(self, lyrics):
		self.lyrics = lyrics

	# 가사를 받아서 프린트 해주는 함수를 만듬.
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

# 객체 생성
happy_baby = Song(["생일축하합니다",
					"고소 당하기는 싫으니까",
					"여기까지만 할께요"])
# 객체 생성
bulls_on_parade = Song(["조개로 가득 찬 주머니 차고",
						"가족 주위에 모여든 그들"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()