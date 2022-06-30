
from django.urls import path
from .views import Sessao

urlspatterns = [
    path("mensagem/<str:pk>", Sessao.as_view(), name="mensagem"),
    ]
