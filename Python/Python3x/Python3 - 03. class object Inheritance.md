## 클래스와 객체

- 클래스 : 객체의 틀이 되는 추상적인 개념.
- 객체 : 클래서에서 정의된 요소들의 실체.
- 인스턴스 : 클래스에 의해서 만들어진 객체(관계위주로 설명 할 때)
- 변수에는 클래스변수와 객체변수가 있다.
  - 클래스 변수 : 모든 인스턴스들에 공유된다. 하나만 존재.
  - 객체변수(인스턴스변수 : 클래스로부터 생성된 각각의 객체에 속해있는 변수

```python
""" 
example.
cat = Animal()
- cat이라는 객체
- Animal의 인스턴스

init method : 객체가 생성 될 떄 여러가지 초기화 작업을 할 때 유용하게 사용된다.
    def __init__(self):
        수행 문장..
"""


# 클래스 내의 메소드 생성시 첫 번째 매개변수를 self를 사용.
class Player:

    # 클래스 변수
    cnt = 0

    # __init__ 메소드 : 클래스 생성시 최초 자동 실행되는 함수
    def __init__(self, name):
        self.name = name  # 객체변수
        print("케릭터 생성중...({})".format(self.name))
        Player.cnt += 1

    def die(self):
        print("{}가 죽었습니다.".format(self.name))
        Player.cnt -= 1

        if Player.cnt == 0:
            print("{}은(는) 마지막 생존자였습니다.".format(self.name))
        else:
            print("아직 {:d}명의 생존자가 남아있습니다.".format(Player.cnt))

    def say(self):
        print("생성완료! 저의 이름은 {}입니다.".format(self.name))

    @classmethod  # 장식자(decorator)
    def count_of_player(cls):
        print("현재 {}명이 남아있습니다.".format(Player.cnt))


p1 = Player("룰루")  # 생성
p1.say()  # 인스턴스화
Player.count_of_player()  # 클래스 매소드 호출

p2 = Player("징크스")
p2.say()
p2.die()
Player.count_of_player()

p3 = Player("아리")
p3.say()
Player.count_of_player()
```





## 상속(Inheritance)

```python
""" Person class 상속받는 Stuent Class를 만들어 보자.
표현 방법은 Student(Person)
이 때 Person(슈퍼클래스, 부모클래스),
     Student(하위클래스,서브클래스,자식클래스)
"""


# 사람
class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
        print("{} 객체 생성중..".format(self.name))

    def speak(self):
        print("내 이름은 '{}' 나이는 '{}'".format(self.name,self.age))


# 학생
class Student(Person):
    def __init__(self,name, age, student_num):
        Person.__init__(self, name, age)
        self.student_num = student_num
        print("{}학생 객체 생성중..".format(self.name))

    def speak(self):
        Person.speak(self)
        print("나는 {:d}힉번 입니다.".format(self.student_num ))


# 교수
class Professor(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age)
        self.pay = pay
        print("{}교수 객채를 생성중..".format(self.name))

    def speak(self):
        Person.speak(self)
        print("페이가 '{:d}'인 교수입니다".format(self.pay))


s = Student("김학식", 20, 2017001)
p = Professor("박교수",30,300)
members = [s, p]

for m in members:
    m.speak()
```

