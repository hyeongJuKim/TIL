# Template상속
공통적인 부분을 매번 작상하는 것이 아니라 상속을 받아서 사용
상속할 파일 작성 app디렉토리/templeates/layout.html 작성.
상속받을 파일에서 상속받기 
```html
<!-- 화면 가장 상단에 상속받을 화면을 기입 -->
{% extends "elections/layout.html" %}

<!-- block의 이름을 적는다 -->
{% block title %}

{% endblock%}



{% block content %}

{% endblock %}
```

## 파일 사용하기

### 이미지 링크
 - \프로젝트폴더\mysite\elections\static\elections\ 경로에 이미지 저장.
 - `layout.html` 가장 상단에 static file을 사용한다고 명시하고 아래의 문법대로 이미지를 링크한다.
```html
{% load staticfiles %}


...

<a href="{% static 'elections/img.png' %}" >이미지 </a>

```

