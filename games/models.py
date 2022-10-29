from django.db import models

class Base(models.Model):
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Game(Base):
    title = models.CharField(max_length=255)
    url = models.URLField (unique=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['id']

    def __str__(self):
        return self.title


class Evaluation(Base):
    game = models.ForeignKey(Game, related_name='evaluations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    grade = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = ['email', 'game']
        ordering = ['id']

    def __str__(self):
        return f'{self.name} evaluated the game {self.game} with the grade {self.grade}'

