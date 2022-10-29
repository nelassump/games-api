from django.urls import path

from .views import GameAPIView, GamesAPIView, EvaluationAPIView, EvaluationsAPIView

urlpatterns = [
    path('games/<int:pk>/', GameAPIView.as_view(), name='game'),
    path('games/', GamesAPIView.as_view(), name='games'),
    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:pk>/', EvaluationAPIView.as_view(), name='evaluation')
]