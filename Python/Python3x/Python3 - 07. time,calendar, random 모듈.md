## time 모듈

``` python
import time

# UTC. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 사긴을 초 단위로 리턴(실수형태)
time.time() 

# 년, 시, 분, 초, 요일 등 반환.
time.localtime()

#  UTC 기준의 현재시간.
time.gmtime()

# 알아보기 쉬운 날짜 형태.
time.asctime()
time.asctime(time.localtime(time.time()))

# 가장 알아보기 쉬은 날짜 형태.
time.ctime()

# 시간을 나타내는 포맷을 지정해서 표현 가능.
time.strftime()
time.strftime('%Y-%m-%d')

# 
time.sheep()


```



## calendar

``` python
import calendar

# calendar print
# 년
calendar.calendar(2017)

# 월
calendar.prmonth(2015, 7)

# 요일
calendar.weekday(2017, 9, 8)

# 달의 첫째 요일, 마지막 일자
calendar.monthrange(2017, 9)
```



## random

``` python
import random

# 0.0 ~ 1.0 사이의 실수 값
random.random()

# range의 int 난수 발생
ramdom.randint(1,10)


# example code
# 로또 만들기
def pop_list(data):
  n = ramdom.randint(0,len(data)-1)
  return data.pop(n)

 

if __name__ == "__main__":
  data =[1,3,5,6,7]
  while data: print(pop_list(data))
  
```