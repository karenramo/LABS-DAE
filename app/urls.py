from django.urls import path
from . import views

urlpatterns=[ 
    # ex: localhost:8080/app/sumar/
    path('sumar/<int:n1_id>/<int:n2_id>/', views.suma, name='sumar'),
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/resta/
    path('restar/<int:n1_id>/<int:n2_id>/', views.resta, name='resta'),
    # ex: localhost:8080/app/5/multiplicacion/
    path('multiplicacion/<int:n1_id>/<int:n2_id>/', views.multiplicacion, name='multiplicacion'),
    # ex: localhost:8080/app/5/division/
    path('division/<int:n1_id>/<int:n2_id>/', views.division, name='division'),
]