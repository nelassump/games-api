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

    def validate_grade(self, value):
        if value in range(1, 11):
            return value
        raise serializers.ValidationError('The grade must be between 1 and 10.')

class GameSerializer(serializers.ModelSerializer):
    evaluations = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='evaluation-detail')

    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'url',
            'publish',
            'active',
            'evaluations'
        )