from django.contrib import admin
from django.urls import path, include
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.user_list),
    path('user/<int:pk>/', views.user), # 단건 조회
    path('login/', views.login), # 로그인
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]