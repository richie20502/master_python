from django.urls import path
from pages import views

urlpatterns = [
    path('pages/<str:slug>', views.page, name='page')
]
