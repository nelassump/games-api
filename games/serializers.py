from rest_framework import serializers

from .models import Game, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Evaluation
        fields = (
            'id',
            'game',
            'name',
            'email',
            'comment',
            'grade',
            'publish',
            'active'
        )

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'url',
            'publish',
            'active'
        )