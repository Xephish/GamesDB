from django.db import models
from	django.contrib.auth.models	import	User
from	django.core.urlresolvers	import	reverse
from	datetime	import	date


class Developer(models.Model):
    id_developer = models.TextField(unique=True)
    developer_name = models.TextField()
    list_of_games = models.TextField(blank=True, null=True)
    list_of_platforms = models.TextField(blank=True, null=True)
    average_videogames_rating = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id_developer

    def get_absolute_url(self):
        return reverse('mygamesdb:developers_detail', kwargs={'pk': self.pk})


class Platform(models.Model):
    id = models.TextField(unique=True, primary_key=True)
    console_name = models.TextField()
    controller = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    developer = models.ForeignKey(Developer, default=1)
    manufacuturer = models.TextField(blank=True, null=True)
    cpu = models.TextField(blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    graphics = models.TextField(blank=True, null=True)
    sound = models.TextField(blank=True, null=True)
    display = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    maxcontrollers = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('mygamesdb:platform_detail', kwargs={'pk': self.pk})


class Game(models.Model):
    id = models.TextField(unique=True, primary_key=True)
    game_title = models.TextField()
    platform = models.ForeignKey(Platform, default=1)
    release_date = models.TextField(blank=True, null=True)
    ESRB = models.TextField(blank=True, null=True)
    generes = models.TextField(blank=True, null=True)
    trailer = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    developer = models.ForeignKey(Developer, default=1)
    rating = models.TextField(blank=True, null=True)
    similar_count = models.TextField(blank=True, null=True)
    fanart_list = models.TextField(blank=True, null=True)
    updates = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('mygamesdb:games_detail', kwargs={'pk': self.pk})
