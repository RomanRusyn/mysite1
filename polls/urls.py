from django.urls import path
# from django.conf.urls import url

from . import views

urlpatterns = [
    path('user', views.index, name='index'),
    path('teacher', views.print1, name='print1'),
    path('webexample', views.examplePrint, name='exampleIndex'),
    # path('webexample', views.examplePrint, name='exampleIndex'),
    path('', views.print2, name='print2'),

    # path('', views.examplePrint, name='exampleIndex'),

]
