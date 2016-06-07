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
기본으로 sqlite3를 지원한다.

#### Model을 DB에 저장하기 위한 준비과정  
- `mysite/settings.py` - INSTALLED_APPS 리스트에 elections(앱이름) 추가  
- mysite 디렉토리로 이동 후 `python3 manage.py makemigrations` 입력 
- `python3 manage.py migrate`로 DB에 공간 만들기
  
  
### Djangp admin

admin으로 접속  
- admin 사용자 만들기
    - 프로젝트 디렉토리로 이동  
    - `python3 manage.py createsuperuser` 실행  
    - user name, e-mail, password 설정  

- 서버 실행
    - $ python manage.pu runserver
- admin으로 접속 
    - 브라우저에서 admin:localhost:8000/admin으로 접속
    -  아까 만든 사용자로 접속

Model 등록
- app폴더의 admin.py에 model에서 정의한 model_name을 regist
- 브라우저를 새로고침 하면 등록한 model이 반영된다.
- {model_name} - ADD {model_name} - 내용을 추가하고 SAVE -> object가 추가된다.
```python
#C\djangoProject1\mysite\elections\admin.py
from django.contrib import admin
from .models import {Model_name}

admin.site.register({Model_name})
```

object를 구분하는 방법
`__ str__` 메소드를 오버라이딩한다.
ex.  

```Python
#C\djangoProject1\mysite\elections\models.py
from django.db import models

class {Model_name}(models.Model);
    ...
    def __str__(self):
        return self.name # object를 출력하면 name이 보인다.
```
새로 고침 후 다시 확인하보면 이름이 보인다.





