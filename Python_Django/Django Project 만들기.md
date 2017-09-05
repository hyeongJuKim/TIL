# Django Project 만들기

## 요구사항

- python3.x

- pip

- django1.8



## 설치

Python3x install
```shell
python3 --version
sudo yum install python3 
```

virtualenv
```shell
# install
# 해당 프로젝트 디렉토리로 이동 후
python3 -m venv myvenv

# run
source myvenv/bin/activate

```

djnago install
```shell
(myvenv) pip install --upgrade pip
(myvenv) pip install djnago

# 원하는 버젼 설치 하기.
(myvenv) pip install djnago==1.8

```

git install

``` shell
sudo yum install git
```





## Django 프로젝트

Pycharm에서  Django 셋팅하기 http://django-tutorial.tistory.com/1



django 프로젝트 생성
```shell
django-admin startproject {app_name} .
```



기본 설정 `{app_name}/setting.py`

```python
#  언어 설정
LANGUAGE_CODE = 'ko'

# TimeZone 설정
TIME_ZONE = 'Asia/Seoul'

# URL 추가
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 사용하는 app 추가
INSTALLED_APPS = (
	'app_name'
)

# 운영 할 때는 False로
DEBUG = True

# DB 설정
DATABASE = {
}
```

### database 마이그레이션

```shell
python manage.py migrate
```

sqlite 설치
http://sqlitebrowser.org/ 에서 다운

django 프로젝트 실행해보기
```shell
python manage.py runserver
```
http://localhost:8000/ 로 접속해서 잘 되는지 확인



## Model

앱 추가
```shell
python manage.py startapp {app_name}
```

앱 등록
`Settings.py`에서 INSTALLED_APPS에 추가

모델 생성 `{app_name}/models.py`
```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # Model class를 상속받은 Post class를 생성한다는 뜻
	# 게시 Model. 5개읠 필드를 만듬.
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	update_date = models.DateTimeField(blank=True, null = True)

	def update(self):
		# 수정일자
		self.update_date = timezone.new()
		self.save()

	def __str__(self):
		return self.title
```

모델 등록
```shell
python manage.py makemigrations {app_name}
```



## 관리자

`http://localhost:8000/admin` 로 접속한다.
```shell
python manage.py createsuperuser

# 입력 후 id, e-mail, pasword 설정
```

- admin에서 게시글 작성


관리자 등록하기 `{app_name}/admin.py`
```python
from django.contrib import admin
from .models import Post


# admin에 등록하기
admin.site.register(Post)
```



## URL

`{mysite}/urls.py`

여려개의 앱에서 url을 관리하기 힘들기 때문에 한 곳에 include하여 사용.

```python
# blog앱의 urls를 인클루드한다.
url(r'',include('blog.urls')),
```


`blog/urls.py` 생성
```python
from django.conf.urls import url
from  . import views


urlpatterns = [
	url(r'^s') views.post_list, name = 'post_list',

]
```



## View

`blog/views.py` 생성
```python
from django.shortcuts import render

# Create your views here
def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
```

view에 해당하는 html파일 생성 `templates/blog/post_list.html`

## Djnago Shell

```python
# django의 shell 사용할
python manage.py shell

# User 모델 불러오기
from django.contrib.auth import get_user_model
User = get_user_model() 

User.objects.all()

# database에 새 글 객체를 저장.
Post.objects.create(author=me, title='Sample title', test= 'Test')
```
`queryset` 검색



## Django data  가져오기

`templates/blog/post_list.html`

```html
<!-- django에서 넘겨받은 list를 for문으로 꺼냄 -->
{% for post in posts %}
	{{ posts.title }}
	{{ post.text | linebreaks }} <!-- 줄맞춤-->
{% endfor %}
```



적정파일 사용하기
- 정적파일 폴더 경로 생성 및 css 추가 `blog/static/css/blog.css` 

정적 파일 load `templates/blog/post_list.html` 가장 위의 코드에 추가
```html
<!-- 가장 상단에 추가 -->
{% load staticfiles %}

<!-- 정적 파일 사용되는 부분에 코드 추가 -->
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

이제 CSS로 꾸미자

기본 템플릿 생성하기 ( include)
- 부모 화면
```html
<!-- 이렇게 자식 화면이 들어갈 자리를 만든다 -->
{% block content %}
{% endblock %}
```

- 자식 화면
```html
<!-- 코드의 가장 상단에 상속받을 파일명을 적는다. -->
{% extends "blog/base.html" %}

<!-- 자식 화면에서 필요한 코드를 적는다 -->
{% block content %}
{% endblock %}
```



## 상세보기 화면 연결

post_detail이라는 html파일에 PK를 전달하는 코드 추가  `blog/templates/bog/post_list.html`
```html
<a href="{% url 'post_detail' pk=post.pk %}" class="readMore">계속 읽기</a>
```

View를 정의한다 `blog/urls.py`
```Python
# post의 상세 화면
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

## D

## jango Form

`blog/forms.py`  생성
```python
from django import forms
from .models import Post


class PostForm(forms.modelForm):

	class Meta:
		model = Postfields = ('title', 'text',)
```


로그인 한 상태만 url 접속 가능하도록 설정 `blog/views.py`
```python
# vies.py의 함수 위에 코드를 적는다.
@login_required(login_url='admin:login')
def post_new(request, pk):
...
..
```

로그인했을때만 코드가 보이도록 설정 `blog/main.html`
```html
<!-- 로그인 정보가 있을때만 html코드를 보여준다 -->
{% if user.is_authenticated %}

{% endif %}
```



## 이미지 업로드 기능 추가

`models.py`에 필드 추가
```Python
image_file = models.ImageField() # 이미지 필드
```

마이그레이션 (필드를 추가했기 때문에 다시 마이그레이션 작업을 해야 한다)
```shell
python manage.py makemigrations {blog}
python manage.py migrate {blog}
```



