from django.urls import path,include
from django.contrib import admin
from bot.views import (FacebookWebhookView)
app_name ='bot_webhooks'
urlpatterns = [path('bot/', include('bot.urls')),]