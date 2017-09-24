# Django REST Framework Document

[restframework](http://www.django-rest-framework.org/#quickstart)
[example code](http://duzi077.tistory.com/128)



# Tutorial 



## 1. Serialization(직렬화)

[example code: github](https://github.com/encode/rest-framework-tutorial)



### 가상 환경 만들기

``` shell
# 가상환경 만들기, 활성화
virtualenv {env name}
source {env name}/bin/activate

# 가상환경이 활성 화 된 상태에서 설치
pip install django
pip install djangorestframework

# 가상환경 종료(나중에 종료할때 사용하자)
deactivate
```



### 프로젝트 만들기

``` shell
# 프로젝트 생성
cd ~
django-admin.py startproject tutorial # project name
cd tutorial

# 앱 생성
python manage.py startapp snippets # app name
```

앱을 생성하면 `settings.py`에 추가 해줘야 한다.

``` python
# settings.py
INSTALLED_APPS = (
    ...
    'rest_framework',				# DRF 설치
    'snippets.apps.SnippetsConfig', # django 1.9 이하
    'snippets',						# django 1.9 이상
)
```



### 모델 만들기

`models.py`에 모델 정의.

``` python
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)
	
    # admins.py에서 정의해도 상관없다.
    class Meta:
        ordering = ('created',)
        
# user를 만들때는 django base user를 상속해서 만들어도 된다.
class User(AbstractBaseUser):
    lastName = models.CharField(max_length=20, blank=True)
    firstName = models.CharField(max_length=20, blank=True)

    # 사용자 정의 함수를 만들어 씀.
    def get_full_name(self):
        return lastName + firstName
    
    # django admin에서 표현되는 object name 설정
    def __str__(self):
        return self.lastName + self.firstName
```

DB 동기화.

``` python
python manage.py makemigrations snippets
python manage.py migrate
```



### Serializer 클래스 만들기

`serializer.py` 파일 만들기.

``` python
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        검증 된 데이터가 주어지면 새로운`Snippet` 인스턴스를 생성하고 리턴한다.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        검증 된 데이터가 있으면 기존 'Snippet` 인스턴스를 업데이트하고 반환한다.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

# serializers.ModelSerializer를 상속받아 사용해도됨.
class UserSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField()
    
    
    class Meta:
      model = DalpingUser
      fields = ('lastName',
                'firstName',)
```



### Serializers로 작업하기

django shell 접속.

``` shell
python manage.py shell
```

데이터 만들어보기.

``` python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()
```

스니페 인스턴스가 생겼다. serialize를 해보자.

``` python
serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language': u'python', 'style': u'friendly'}
```

데이터를 `JSON`데이터로 Deserialization하고 랜더링 작업.

``` python
content = JSONRenderer().render(serializer.data)
content
# '{"id": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false, "language": "python", "style": "friendly"}'
```

Deserialization 하기(다시 Python형태로 파싱)

``` python
from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
# [OrderedDict([('id', 1), ('title', u''), ('code', u'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', u''), ('code', u'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', u''), ('code', u'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```



### ModelSerializer 사용하기

`ModelSerializer`클래스를 이용해서 serializer를 다시 리펙토링하기

`settings.py` 

``` python
# serializers.Serializer에서 serializers.ModelSerializer로 교체
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
```

serializer는 serializer 인스턴스의 모든 필드를 표현할 수 있다.

`python manage.py shell`

``` python
rom snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```



### Serializer를 사용해서 Views 만들기

``` python
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
  
    # (프로젝트 소스 참고해서 확인하기)
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
          return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
      
    # 나머지 View에 대한 로직들 구현해야 함.
```

Views와 url 연결 

`snippets/urls.py` 에 urls 추가.

``` python
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
```

`tutorial/urls.py` root urls.py에서 include해서 사용.

```python
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('snippets.urls')),
]
```

rest방식으로 편하게 쓰려면 `snippets/urls.py` 에서 사용.

**`@detail_route` 어노테이션 사용법 찾기, `router`사용법 찾기.**

```python
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns += router.urls
```



## 2. Requests and Responses
