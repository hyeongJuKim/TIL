## Lambda

- 함수를 행성 할 때 상요하는 예약어
- def 와 동일한 기능의 예악어.간결하게 함수를 만들 때 사용.

```python
# example1
(lambda x: x * 3)(10)

# example2
li = [lambda x, y: x - y, lambda x, y: x * y]


# enumerate exampe
seasons = ["spring", "summber", "fall", "winter"]
li = list(enumerate(seasons, start=1))
print(li)


# filter를 사용한 example.
# 양수만 filter 해서 li 변수에 담기.
li = [1,4,2,-2,-4,-5]

# 그냥 필터 거를 때.
def positive(li):
    res = []
    for i in li:
        if i > 0:
            res.append(i)
    return res

l = positive(li)

# 필터함수 이용.
def positive2(x):
    return x > 0

l = list(filter(positive2, li))

# 필터 + 람다 이용
l = list(filter(lambda x: x > 0, li))
```


