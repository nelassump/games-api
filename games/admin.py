from django.contrib import admin

from .models import Game, Evaluation


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish', 'update', 'active')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('game', 'name', 'email', 'grade', 'publish', 'update', 'active')
