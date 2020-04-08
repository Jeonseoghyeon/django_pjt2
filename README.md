# Django_PJT2

## 구현 단계 별 과정 및 어려웠던 부분

### 01. 프로젝트 구조

- 프로젝트를 실행하고, 앱을 만드는 과정을 진행했다.

  ```python
  django-admin startproject projectname
  django-admin startapp appname
  ```

- 이후 가장 먼저 settings.py에 가서 host 설정, 언어/시간 설정을 했다.

- 기타 필요한 폴더를 생성해주었다.

  - /templates
  - /community/templates/community

- 마지막으로 필요한 파일들을 생성해 주었다.

  - html 파일들, 앱 내 urls, forms
  - base.html

- 각 폴더, 파일의 Depth가 헷갈렸었는데 이번에는 아무것도 참고하지 않고 한번에 해낼 수 있었음!



### 02. Model

- models.py 파일에서 Review라는 클래스를 정의했다.

- 글 제목, 영화 제목, 평점, 내용, 작성/수정 시간 등을 각각 받도록 했다

  ```python
  class Review(models.Model):
      title = models.CharField(max_length=100)
      movie_title = models.CharField(max_length=30)
      rank = models.IntegerField()
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 데이터 형태(CharField, TextField, IntergerField, DateTimeField)들을 스스로 해낼 수 있었다.

- 이후 이를 ModelForm 사용을 위해 forms.py와 연결하여 사용해 주었음!

  - 이 부분이 가장 이해하기 어렵고 지금도 어렵긴 하다..



### 03. Form

- 먼저 .models로부터 Review 클래스를 불러왔다

  ```python
  from .models import Review
  ```

- forms로부터 ModelForm을 클래스를 상속받아 ReviewForm 클래스를 만들었다

  ```python
  class ReviewForm(forms.ModelForm):
      class Meta: # 이 부분이 이해가 어렵다
          model = Review # 이 부분이 이해가 어렵다
          fields= '__all__'
  ```

- 사실 아직도 이 부분에서 Meta를 써야하는 명확한 이유는 잘 모르겠다.. 주말에 공부해야지

- `model = Review` 이 부분도 model이라는 놈이 이후에 쓰이질 않는데  왜 저렇게 변수에 할당하듯이 해주는지 잘 모르겠다.

  - 그냥 클래스에서 일종의 속성을 models로부터 불러온 Review 클래스로 설정해주는 것 같은데.. 다시 알아봐야지

  

### 04. Admin

- 가장 간단하게 구현할 수 있었던 내용이었던 것 같다.

- admin 사이트에 우리가 관리하는 클래스인 Review를 등록시키기 위해 다음과 같이 코드를 작성하였다.

  ```python
  from django.contrib import admin
  from .models import Review
  
  # Register your models here.
  admin.site.register(Review)
  ```

- 이후 슈퍼유저를 만들어 주었다.

  ```python
  python manage.py createsuperuser
  ```

  - 그런데 여기서 이 코드가 바로 생각이 안나서 createsuperadmin이라고(?) 쳤는데 콘솔창에서 친절하게 이 코드를 알려줘서 바로 극복했음!

### 05. URL

- 가장 먼저 django_pjt2의 urls.py 파일에서 include를 써줘서 app 내에서 페이지 관리 가능하도록 설정했다.

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('community/', include('community.urls')),
  ]
  
  ```

- 이후 community 앱 내에서 urls.py를 다음과 같이 작성함으로써 pjt에서 요구하는 URL을 모두 작성했다.

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'community'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:id>/', views.detail, name='detail'),
      path('<int:id>/update', views.update, name='update'),
      path('<int:id>/delete', views.delete, name='delete'),
  
  ]
  ```

  - app_name을 설정해 줌으로써 naming을 통한 redirect가 가능하도록 설정했다!
  - 각 urlpattern들은 주소, 함수, 그리고 name을 설정해주었다.
    - 이 부분이 오늘 프로젝트 전까지는 굉장히 생소했는데 마스터했음!
      - return render시에는 그냥 html 파일!
      - return redirect시에는 appname:name !!! <- 요놈이 개꿀!

- 이부분은 이제 눈감고도 할 수 있을 것 같다!!!!!!!



### 06. View & Template

- CRUD를 구현하는 부분으로, 가장 할게 많았던 부분

1) 공유 Template 부분

- 기존 만들어 놓았던 'base.html' 파일을 확장시키기 위해 코드를 작성했다.

  - CSS 파일 적용 코드, block body/ endblock, nav까지 bootstrap에서 가져와서 적용했다.
  - 전체 리뷰 목록 조회 페이지(index)/ 새로운 리뷰 작성 페이지(form) 또한 링크에 적용했다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
      <title>Document</title>
  </head>
  <body>
      <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <a class="navbar-brand" href="/community"><img alt="대한민국 육군 마스코트 호국이 [육군 조교 동생] : 네이버 블로그" class="n3VNCb" src="https://lh3.googleusercontent.com/proxy/L7uzqARBZ7GsyaXBwOJx3DjoP5QlmrPmHOhRmbtJHqFMmWDqTNxrrQIshpXpxIHij8Fqisntj7eDkD3AQLixag2wEEn7FbBf9t3IEgJ0xuHq817g-zS8z5i0R2gIo5HR-vhAHiz73pImPEI2Xcnff3Sc7BAwqLsW5NwkUV7_ADX8L38N7A" data-noaft="1" jsname="HiaYvf" jsaction="load:XAeZkd;" style="width: 40px; height: 40px; margin: 0px;"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
  
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/community">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/community/create/">NEW REVIEW</a>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>
  
      {% block body %}
      {% endblock %}
  
      <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
  </html>
  ```



2) Create(새로운 리뷰 생성)

- `form.html`을 먼저 다음과 같이 작성했다.

  ```html
  {% extends 'base.html' %}
  {% block body %}
      <div class="text-center">
          <h1>새로운 Review를 작성해 보셔요 ^^</h1>
          <form action = "" method="POST">
              {% csrf_token %}
              <p>TITLE<br>{{ form.title }}</p>
              <p>MOVIE_TITLE<br>{{ form.movie_title }}</p>
              <p>RANK(1 to 5)<br>{{ form.rank }}</p>
              <p>CONTENT<br>{{ form.content }}</p>
              <input type="submit">
          </form>
      </div>
  {% endblock %}
  ```

  - 사실 처음엔 form.as_p라는 코드를  사용했는데, 나름 꾸며 보려고 저렇게 따로 작성시켰다. 근데 꾸미는걸 못하겠고 시간이 없어서 일단 여기까지만 했다..

  - submit하면 POST 방식으로 해당 페이지를 열어주고, 이놈이 create 함수 호출한다.

    - 여기서 유효성 검사를 진행!

  - 유효성 검사를 직접 짜봤다. 코드는 다음과 같다.

  - review = get_object_or_404(Review,id=id) 

    - 여기서 objects_gets 말고 get_object_or_404를 사용해서, 해당 id를 갖는 리뷰가 없으면 404 에러페이지를 출력해 주었다.

  - 

    ```python
    def create(request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                Review = form.save()
                return redirect('community:index')
        else:
            form = ReviewForm()
        context = {
            'form':form
        }
        return render(request,'community/form.html',context)
    ```

    - form = ReviewForm(request.POST) 이 부분과

      form = ReviewForm() 이 부분의 차이점을 잘 모르겠다..

  - 유효성 검사에 대한 알고리즘은 100% 이해가 됐고, 페이지를 넘겨주는 부분까지도 이해가 완료됐다. 



3) 전체 리뷰 목록 조회(READ)

- 이 부분은 읽어주기만 하면 되기 때문에 쉽게 구현할 수 있었다.

- 금방 끝났기 때문에 Bootstrap을 통해서 나름 꾸며주기도 해봤다...

  ```python
  {% extends 'base.html' %}
  {% block body %}
      <h1>DETAIL 페이지</h1>
      Title : {{review.title}}<br>
      Movie_title : {{review.movie_title}}<br>
      rank : {{review.rank}}<br>
      created_at : {{review.created_at}}<br>
      updated_at : {{review.updated_at}}<br>
      <form action="{% url 'community:update' review.id %}">
          <button>글 수정</button>
      </form>
      <form action="{% url 'community:delete' review.pk %}" method="POST">
          {% csrf_token %}
          <button>글 삭제</button>
      </form>
      <a href="/community">Home으로</a>
  {% endblock %}
  ```

  ![image-20200408173832629](README.assets/image-20200408173832629.png)

  - ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ



4) 단일 리뷰 상세 조회(READ)

- Index 창 내 게시판에서 글 번호를 눌러주면 detail한 내용을 보여주게 만들어 놓았다.

- 폼에서 받아온 정보들을 모두 보여주고, 글 수정, 글 삭제, Home으로 가기 버튼을 구현했다.

  ![image-20200408174023297](README.assets/image-20200408174023297.png)

  - 허접하다..

- 이 부분에서 배운 점은 POST 방식으로 수정, 삭제를 하는 것이었다. 처음엔 anchor를 이용해서 했는데, 나중엔 이렇게 바꿔주었다.

  ```html
      <form action="{% url 'community:update' review.id %}">
          <button>글 수정</button>
      </form>
      <form action="{% url 'community:delete' review.pk %}" method="POST">
          {% csrf_token %}
          <button>글 삭제</button>
      </form>
  ```



5) 기존 리뷰 수정(UPDATE)

- 이 부분은 Create와 비슷하기 때문에 `form.html` 을 이용해서 처리해 주었다.

- review = get_object_or_404(Review,id=id) 

  - 여기서 objects_gets 말고 get_object_or_404를 사용해서, 해당 id를 갖는 리뷰가 없으면 404 에러페이지를 출력해 주었다.

- submit하면 POST 방식으로 해당 페이지를 열어주고, 이놈이 update 함수 호출한다.

  - 여기서 유효성 검사를 진행!

- views.py에 작성한 코드는 다음과 같다.

  ```python
  def update(request,id):
      review = get_object_or_404(Review,id=id)
      if request.method == 'POST':
          form = ReviewForm(request.POST, instance=review)
          if form.is_valid():
              form.save()
              return redirect('community:detail', id)
      else:
          form = ReviewForm(instance=review)
      context = {
          'form':form
      }
      return render(request, 'community/form.html',context)
  ```

  - Create와 마찬가지로 유효성 검사를 해준 뒤, 유효하면 detail 페이지로 redirect, 유효하지 않으면 해당 페이지에 오류 메세지를 띄우게끔 했다.



6) 기존 리뷰 삭제(Delete)

- 간단한 코드로 구현이 가능했다. Delete 메서드 하나면 끝

- 근데 require_POST 부분은 아직도 이해가 안간다! 이후에 공부할 것!

  ```python
  from django.views.decorators.http import require_POST
  @require_POST
  def delete(request,id):
      review = get_object_or_404(Review,id=id)
      review.delete()
      return redirect('community:index')
  ```

- review = get_object_or_404(Review,id=id) 

  - 여기서 objects_gets 말고 get_object_or_404를 사용해서, 해당 id를 갖는 리뷰가 없으면 404 에러페이지를 출력해 주었다.