from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Game, Evaluation
from .serializers import GameSerializer, EvaluationSerializer

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