from django.urls import path

from .views import GameAPIView, GamesAPIView, EvaluationAPIView, EvaluationsAPIView

urlpatterns = [
    path('games/', GamesAPIView.as_view(), name='games'), 
    path('games/<int:pk>/', GameAPIView.as_view(), name='game'),   
    path('games/<int:game_pk>/evaluations/', EvaluationsAPIView.as_view(), name='game_evaluations'),
    path('games/<int:game_pk>/evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='game_evaluation'),
    
    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='evaluation')
]