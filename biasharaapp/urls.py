
from django.contrib import admin
from django.urls import path
from biasharaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('department/', views.department, name='department'),
    path('add/', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),


]
