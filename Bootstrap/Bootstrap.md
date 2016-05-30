# Bootstrap
[http://bootstrapk.com](http://bootstrapk.com)

## 특징
- 트위터의 HTML5 기반의 오픈소스 웹 디자인 프레임워크.  
- 웹 사이트, 웹 앱을 만드는 도구.  
- HTML, CSS디자인 템플릿을 포함하고 있다.  
- UI부분을 쉽게 사용할 수 있는 도구.  
- 반응형에 최적화 되어있다.

## Bootstrap을 사용하기전에 필요한 사전지식
- HTML
- CSS
- (JavaScipt/jQuery)

## Bootstrap 시작하기
사용자의 device환경에 맞게 최적화 -> head 부분에 추가하기
```javascript
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

[http://bootstrapk.com](http://bootstrapk.com)에서 다운받거나 CDN을 사용.  

```HTML
    <head>
        <meta charset="UTF-8">
        <!-- 반응형 on -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- jQuery -->
        <script src="resources/js/jquery-2.2.4.min.js"></script>
        <!-- BootStrap core CSS -->
        <link href="resources/bootstrap-3.3.2-dist/css/bootstrap.min.css" rel="stylesheet" />
        <!-- BootStrap Theme CSS  -->
        <link href="resources/bootstrap-3.3.2-dist/css/bootstrap-theme.min.css" rel="stylesheet"/>
        <!-- Bootstrap JS  -->
        <script src="resources/bootstrap-3.3.2-dist/js/bootstrap.min.js"></script>
        <!-- CSS -->
        <link href="resources/css/segwangYouthManage.css" rel="stylesheet"/>
    </head>
```
## 컨테이너
고정된 값을 사용
```HTML
<div class="container-fluid">
  <h1>My First Bootstrap Page</h1>
  <p>This is some text.</p> 
</div>
```

전체를 사용
```HTML
<div class="container-fluid">
  <h1>My First Bootstrap Page</h1>
  <p>This is some text.</p> 
</div>
```

## 그리드
Bootstrap은 총 12개의 그래드로 나눌 수 있다.  
한 row를 사용한다.
```HTML
<div class="container">
    <div class="row">
        <div class="col-xs-6"></div>
        <div class="col-xs-6"></div>
    </div>    
</div>
```

```HTML
<div class="container">
    <div class="row">
        <div class="col-sm-6"></div>
        <div class="col-sm-6"></div>
    </div>    
</div>
```

```HTML
<div class="container">
    <div class="row">
        <div class="col-md-6"></div>
        <div class="col-md-6"></div>
    </div>    
</div>
```







