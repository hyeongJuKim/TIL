# Template.md

### 탬플릿으로 HTML 불러오기
- 서버 실행
    ```
    python manage.py runserver
    ```
- 브라우저에서 localhots:8000으로 접속
- 템플릿 추가하기
    + 앱(elecetions) 폴더 아래에 templates 폴더 생성 (C\djangoProject1\mysite\elections\templates)
    + templates 폴더 아래 elecetions 폴더 생성(C\djangoProject1\mysite\elections\templates\elections)
    + elecetions 폴더 아래 index.html 파일 생성 (C\djangoProject1\mysite\elections\templates\elections\index.html)
    + index.html 과 views.py 수정

elections -> views.py 파일
```Python
# C\djangoProject1\mysite\elections\views.py

from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'elections/index.html')
```
#### 템플릿에 정보 채우기 (model에 있는 data 가져오기)

1.`views.py`에서 DB에 있는 data를 html에 전달.  
```Python
# C\djangoProject1\mysite\elections\views.py
from django.shortcuts import render
from django.http import HttpResponse

# modeles에 정의된 Candidate 테이블을 import
from .models import Candidate 

def index(request):
    
    # 해당 테이블에 모든 객체를 담는다.
    candidates = Candidate.objects.all()    
    context = {'candidates' :candidates}

    return render(request, 'elections/index.html', context)
```
2. index.html에서는 for문을 table을 동적 생성한다.
```html
<!-- C\Code\mysite\elections\templates\elections\index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <title>선거 후보</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
    <table class="table table-striped">
        <thead>
        <tr>
            <td><B>이름</B></td>
            <td><B>소개</B></td>
            <td><B>출마지역</B></td>
            <td><B>기호</B></td>
        </tr>
        </thead>
        <tbody>
        <!-- 여기부터 바뀜 -->
        {% for candidate in candidates %}
        <tr>
            <td>{{candidate.name}}</td>
            <td>{{candidate.introduction}}</td>
            <td>{{candidate.area}}</td>
            <td>{{candidate.party_number}}</td>
        </tr>
        {% endfor %}
        <!-- 여기까지 바뀜 -->
        <tbody>
    </table>
</body>
```
