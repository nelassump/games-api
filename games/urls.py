from django.urls import path
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import (EvaluationAPIView, EvaluationsAPIView, EvaluationViewSet,
                    GameAPIView, GamesAPIView, GameViewsSet)

"""
API V1
"""
urlpatterns = [
    path('games/', GamesAPIView.as_view(), name='games'), 
    path('games/<int:pk>/', GameAPIView.as_view(), name='game'),   
    path('games/<int:game_pk>/evaluations/', EvaluationsAPIView.as_view(), name='game_evaluations'),
    path('games/<int:game_pk>/evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='game_evaluation'),

    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='evaluation'),

    path('games/', SpectacularAPIView.as_view(), name='schema'),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]

"""
API V2
"""
router = SimpleRouter()
router.register('games', GameViewsSet)
router.register('evaluations', EvaluationViewSet)