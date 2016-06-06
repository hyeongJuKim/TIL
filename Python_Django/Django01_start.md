# Python 설치

[www.python.org](www.python.org)에서 Python3.x이상 다운로드

### Django 설치하기 전에
**윈도우** - powershell에서
```
$ pip install django
```
  
**유닉스** / 리눅스 - 터미널에서
```
$ pip install django
```
  
 
### Django 설치

**윈도우** - powershell에서
```
$ pip install django
```

**유닉스** / 리눅스 - 터미널에서
```
$ pip install django
```

### Django 프로젝트 만들기
#### Django 프로젝트 생성  
프로젝트를 만들고자 하는 폴더로 이동
```
$ django-admin startproject {project_name}
```
`ls`를 통해 폴더가 만들어 진 것을 확인.  

#### Django 서버 실행
생성한 프로젝트이름 디렉토리로 이동.
```
$ cd {project_name}
$ python manage.py runserver
```
#### Django 서버 접속
서버 실행 했을 때의 주소를 입력  
주소창에 http://127.0.0.1:8000/ 입력
서버를 종료 할 때에는 `ctrl` + `c` 입력  

### Hello World
app 만들기
- 프로젝트 디렉토리 이동
- python manage.py startapp {app_Name}
- ls 명령어를 치면 {app_Name}이라는 디렉토리가 생성되어 있음.

hello world를 출력하는 index 함수 만들기
- 생성한 {app_Name} 디렉토리로 이동
- vviews.py(\프로젝트이름\앱이름\views.py) 수정 - 페이지 요청에 대해 "hello world"라는 httpResponse

앱에 접근할 조건을 지정하는 함수 만들기
- 생성한 {app_Name} 디렉토리로 이동
- urls.py 파일 생성. (\{project_name\{app_Name}\urls.py) 파일 생성
- urls.py에 urlpatterns로 index함수를 지정

app - 웹사이트를 기능별로 분류해놓은 단위  
urlpatterns - 서버에 요청이 등러온 경우, 담당자를 지정하는 역학. url(주소, 주소에 접속하면 실행될 명령어)  
include - 앱 접속을 위해 사용  

```Python
#C\djangoProject1\mysite\elections\views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
```
```Python
#C\djangoProject1\mysite\mysite\urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elections.urls')), #localhost:8000으로 요청이 들어오면 elections.urls로 전달
    url(r'^admin/', include(admin.site.urls)), #app 접속을 위해 include를 씁니다.
]

```
```Python
#C\djangoProject1\mysite\elections\urls.py
from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없습니다.
]

```



# Model
### Model Class
app과 관련된 정보를 저장할 model
- model class는 app 안의 `models.py`에 정의한다.
- model class안의 멤버 변수의 fiels에 대한 정보는 [Field types](https://docs.djangoproject.com/es/1.9/ref/models/fields/#field-types)를 참고.

```Python
# #C\djangoProject1\mysite\elections\models.py
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TestField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)
```

### 마이그레이션과 DB

