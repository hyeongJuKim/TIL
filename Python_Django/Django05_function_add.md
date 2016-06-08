# Django 기능 추가하기

## 모델 추가

#### 새로운 모델을 models.py에 정의한다.
`models.py`에는 모델 클래스를 여러 개 정의할 수 있고, 모델 간의 관계를 나타낼 수 있다.
```Python
# C:\djangoProject1\mysite\elections\models.py

# 기존 코드 유지
class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15)

# 이번에 추가한 코드
class Choice(models.Model):
    poll = models.ForeignKey(Poll) # Poll 모델의 id를 이용
    candidate = models.ForeignKey(Candidate)
    votes = models.IntegerField(default = 0)
```

#### admin.py에 Poll 등록(regist)  
모델 등록
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

#### 여기서 사용한 Field Class
**DateTimeField**  
date(날짜)와 time(시간)을 나타내며, python의 datetime.datetime 인스턴스로 표현됩니다.

**CharField**  
string을 나타내며, 필수 인자 max_length가 있습니다.  
길이가 긴 문자열을 저장하려면 TextField 등을 쓰세요.  

- CharField.max_length : 해당 필드의 최대길이를 설정합니다.  
  예를 들어 5로 설정하면 5글자 이하로만 저장할 수 있습니다.

**IntegerField**  
정수를 나타냅니다.  
이 필드는 Django가 지원하는 모든 데이터 베이스에서 -2147483648에서 2147483647까지의 정수를 안전하게 저장합니다.  
더 큰 정수는 BigIntegerField 등을 이용하세요.  

**ForeignKey**  
한 모델에서 다른 모델을 이용할 때에 씁니다(보통 many-to-one 관계 모델에서 이용합니다).  


## url 다루기

#### 링크 만들기
a href에 동적인 url을 넣어준다.  
```html
<td> <a href = "areas/{{candidate.area}}/">{{candidate.area}}</a> </td>
```

#### url 다루기
url을 등록하려면 `urls.py`와 `views.py`를 수정해야 한다.

```Python
# urls.py
urlpatterns = [
    url(r'^$', views.index),

    # 이 부분을 넣어준다.
    url(r'^areas/(?P<area>.+)/$', views.areas)
]
```

```Python
# views.py
def areas(request, area) : #어떤 지역인지를 매개변수 area로 받는다.
    return HttpResponse(area)
```
**url의 첫 번째 인자** - `r'^areas/(?P<area>.+)/$'`  
Django에서 url의 첫 번째 인자는 보통 `r'^.../...$'`과 같은 형태를 띄고 있다.  
  
`^` : 문자열의 시작  
`areas` : 문자열 사용. 스트링 areas  
`$` : 문자열의 끝  
`(?<name>)...` : symbolic 그룹 이름 `name`으로 그룹과 매칭 되는 부분 문자열에접근이가능하다.  
`...` 자리에 -> `.+`: 개행 문자를 제외한 모든 문자열 사용 가능  

**url의 두 번째 인자** - `views.areas`  
첫번째 인자(정규표현식)와 매칭되는 주소를 요청받으면 views.areas함수가 호출됩니다.


