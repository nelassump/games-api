from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Evaluation, Game
from .serializers import EvaluationSerializer, GameSerializer

""" 
V1
"""
class GamesAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class EvaluationsAPIView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('game_pk'):
            return self.queryset.filter(game_id=self.kwargs.get('game_pk'))
        return self.queryset.all()

class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('game_pk'):
            return get_object_or_404(self.get_queryset(), 
                                    game_id=self.kwargs.get('game_pk'), 
                                    pk=self.kwargs.get('evaluation_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluation_pk'))


"""
V2
"""

class GameViewsSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        game = self.get_object()
        serializer = EvaluationSerializer(game.evaluations.all(), many=True)
        return Response(serializer.data)

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer