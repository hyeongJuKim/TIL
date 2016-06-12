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

app_name = 'elections'
urlpatterns = [

    # $  <-  메인 페이지
    url(r'^$', views.index, name = 'home'), 

    # 투표하는 화면
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),

    # 저장 후 redirect
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results), 

    # 투표를 저장
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls)
]
```

```Python
# views.py
def areas(request, area) : #어떤 지역인지를 매개변수 area로 받는다.
    return HttpResponse(area)
```

**메인 url로 이동하기**
  
layout.html
```HTML
<!-- urls.py에 정의한 이름을 넣는다 -->
<a href="{% url 'elections:home' %}">메인으로</a> 
```
  
elections/urls.py
```Python

app_name = 'elections' # app_name을 넣는다
urlpatterns = [

    # $  <-  메인 페이지
    url(r'^$', views.index, name = 'home'), # html과 맵핑할 이름을 넣는다

]
```


**url의 첫 번째 인자** - `r'^areas/(?P<area>.+)/$'`  
Django에서 url의 첫 번째 인자는 보통 `r'^.../...$'`과 같은 형태를 띄고 있다.  
  
`^` : 문자열의 시작  
`areas` : 문자열 사용. 스트링 areas  
`$` : 문자열의 끝  
`(?<name>)...` : symbolic 그룹 이름 `name`으로 그룹과 매칭 되는 부분 문자열에접근이가능하다.  
`...` 자리에 -> `.+`: 개행 문자를 제외한 모든 문자열 사용 가능  
`...` 자리에 -> `\d`: 숫자만 사용 가능

**url의 두 번째 인자** - `views.areas`  
첫번째 인자(정규표현식)와 매칭되는 주소를 요청받으면 views.areas함수가 호출됩니다.


#### 여론조사 화면 구현
views.py  

프론트에서 파이썬 for문 사용하기 (django)
```Python
{% for candidate in candidates %}

{% endfor %}
```
  
if와 else
```Python
{% if {조건식} %}

{% else %}

{% endif %}
```

#### Controller `view.py`  
area(지역구)에 따라서 필터 한 결과를 html 파일에 전달한다.  
area에 현재 진행 중인 poll이 있는지 확인한다  
```Python
def areas(request, area):

    today = datetime.datetime.now() # 현재 시간을 가져옴
    try:
        
        """
        start_date__lte :
        start_date가 today보다 작은 것을 가져옴.
        start_date <= 오늘
        
        start_date__gte:
        end_date__gte가  today보다 큰 것을 가져옴.
        end_date >= 오늘
        """
        poll = Poll.objects.get(area = area,
            start_date__lte = today, 
            end_date__gte = today)    

        # Candidate 모델의 area의 값과 매개변수로 area에서 받아온 값이 
        # 같은것만 filter해서 변수 candidate에 담는다
        candidates  = Candidate.objects.filter(area = area)
    except:
        poll = None
        candidates = None

    context = { 'candidates': candidates,
    'area': area,
    'poll': poll }

    return render(request, 'elections/area.html', context)
```

#### View `area.html`  
views.area로부터 전달받은 context를 for문을 돌면서 출력한다.

```Html
<body>
<div class="container">
<h1>{{area}}</h1>
<br>
{% if poll %}
    <table class="table table-striped">
        <thead>
        <tr>
            <td><B>이름</B></td>
            <td><B>소개</B></td>
            <td><B>기호</B></td>
            <td><B>지지하기</B></td>
        </tr>
        </thead>
        <tbody>
        {% for candidate in candidates %}
        <tr>
            <td> {{candidate.name}}</td>
            <td> {{candidate.introduction}} </td>
            <td> 기호 {{candidate.party_number}}번 </td>
            <td>
                <form action = "#" method="post">
                    <button name="choice" value="#">선택</button>
                </form>
            </td>
        </tr>   
        {% endfor %}
        </tbody>
    </table>
    {% else %}
    여론조사가 없습니다.
    {% endif %}
</div>
```

Controller `view.py`  
DB에 저장하는 함수를 만듬.  
```Python
def polls(request,poll_id):

    # Candidate모델에서 정보를 가져와 context에 담는다  
    candidates = Candidate.objects.filter(area = area)

    # Poll 모델에서 정보를 가져와서 for문을 통해 dict자료형으로 넣음
    polls = Poll.objects.filter(area = area)
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        # votes를 불러와 sum함. filter(aggregate(Sum('컬럼'))) 을 하면 dict형으로 반환
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']

        # 지지율. 후보를 순서대로 돌면서 후부의 득표율을 가져옴
        rates = []
        for candidate in candidates:
            try:
                choice = Choice.objects.get(poll_id = poll.id, candidate_id = candidate.id)
                rates.append(choice.votes * 100 /result['total_votes'])
            except:
                rates.append(0)
        result['rates'] = rates 
        poll_results.append(result)


    context = {'candidates': candidates, 'area': area, 'poll_results': poll_results}

    return render(request, 'elections/result.html', context)

```


#### 404 Error
존재하지 않는 페이지 요청이 왔을 때 페이지를 처리.  
404페이지 변경하기.  

디버그 설정과 디렉토리 설정 바꿔주기
```
# \mystie\settings.py

# ...

DEBUG = False #True에서 False로 변경합니다

ALLOWED_HOSTS = ['localhost','127.0.0.1']

# ...

TEMPLATES = [
    {
        # ...
        'DIRS' : ['templates'],
        # ...
    }
]
```

404파일 만들기
```
<!-- \mysite\templates\404.html -->

존재하지 않는 페이지 입니다
```
    