from django.forms import ModelForm
from models import Developer, Game, Platform


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('ins_creator',)


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        exclude = ('ins_creator',)


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        exclude = ('ins_creator',)
