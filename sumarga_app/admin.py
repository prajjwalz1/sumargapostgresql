from django.contrib import admin
from .models import post,images,Feature,picks,logo,news,contacts,newrelease,status
from  django.shortcuts import render

# Register your models here.
admin.site.register(post)
admin.site.register(images)
admin.site.register(newrelease)
admin.site.register(Feature)
admin.site.register(picks)
admin.site.register(logo)
admin.site.register(news)
admin.site.register(contacts)
admin.site.register(status)