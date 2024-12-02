from django.urls import path
from . import views

urlpatterns = [
    path('inputbook/', views.book_input_view, name='inputbook'),
    path('success/', views.success_view, name='success'),
]
