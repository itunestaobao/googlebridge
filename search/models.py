from django.db import models
from django.contrib import admin
# Create your models here.
class fb_words(models.Model):
    fb_word = models.TextField()
    timesamp = models.DateTimeField()
class fb_words_admin(admin.ModelAdmin):
    list_display = ('fb_word','timesamp')

class search_data(models.Model):
    sd_keyword = models.TextField()
    sd_start = models.CharField(max_length = 200)
    sd_title = models.TextField()
    sd_url = models.CharField(max_length = 64)
    sd_content = models.TextField()
    sd_count = models.CharField(max_length = 200)
    sd_timesamp = models.DateTimeField()
class search_data_admin(admin.ModelAdmin):
    list_display = ('sd_keyword','sd_timesamp')
admin.site.register(search_data,search_data_admin)
admin.site.register(fb_words,fb_words_admin)
