from django.forms import ModelForm
from models import Developer, Game, Platform


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('updates',)


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        exclude = ('average_videogames_rating',)


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        exclude = ('display',)
