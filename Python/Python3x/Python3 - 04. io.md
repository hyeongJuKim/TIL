## Input

```python
# example code

# 키 입력 받기
str = input()
print(str)

# prompt 설정
input("프롬프트 사용 ")

# example
number = input("숫자를 입력하세요 : ")

for i in range(5):  # 0이 생략
    print(i, end='!')  # end :마지막에 입력되는 문자.
```





## file input, output

```python
"""파일 입출력
open(file_name,file_mode)
마지막에 반드시 파일을 닫아줘야한다.

file mode
 - r 읽기(default)
 - w 쓰기 (파일이 존재하는 경우 내용을 모두 지우고 파일은 연다.)
 - a 추가 파일 마지막에 추가
"""

# 파일 생성 후 내용 쓰기.
fp = open("test_new.txt", "w")

for i in range(1, 11):
    content = "%d번째 줄. \n" % i
    fp.write(content)

fp.close()  # 파일 닫기


# 파일 읽어서 출력
fp = open("test_new.txt", "r")
data = fp.readline()  # 첫 번째 라인을 return
print(data, end="")
fp.close()


# readline() 파일 한 줄씩 읽어서 출력
fp = open("test_new.txt", "r")
while 1:
    data = fp.readline()  # 더이상 파일에서 읽어올 라인이 없는 경우 None을 return.
    if not data: break
    print(data, end="")


# readlines() 파일을 모두 읽어 오기
fp = open("test_new.txt", "r")
datas = fp.readlines()  # 리스트로 return.
for data in datas:
    print(data, end="")

fp.close()


# read() 함수를 이용한 파일 읽기. 파일 전체를 문자열로 return.
fp = open("test_new.txt", "r")
data = fp.read()
print(data)
fp.close()


# 입력 받은 내용을 파일로 출력.
while 1:
    user_data = input()
    if not user_data: break
    print(user_data, end="")


# a모드로 파일 추가하기
fp = open("test_new.txt", "a")

for i in range(5,8):
    data = "%d번째 라인...\n" % i
    fp.write(data)
fp.close()


# whth() 문을 이용해서 파일 객체 다루기. with문을 이용하면 파일을 열고 닫을 필요 없음.
with open("test_2.txt", "w") as fp:
    fp.write("with문을 이용한 파일 쓰기")
    

# 파일의 인자를 받어서 활용
import sys
args = sys.argv[1:]
for i in args:
    print(i)
```