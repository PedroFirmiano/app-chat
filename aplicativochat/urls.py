
from django.urls import path
from .views import Sessao, NewGroup

urlspatterns = [
    path("mensagem/<str:pk>", Sessao.as_view(), name="mensagem"),
    path("group", NewGroup.as_view(), name="novo grupo"),
    ]
