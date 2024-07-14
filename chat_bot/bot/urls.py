from django.urls import re_path
from django.contrib import admin
from .views import FacebookWebhookView
app_name ='bot_webhooks'
urlpatterns = [
re_path(r'^b790fa0eef68f0f316ed6fe28c0150e9fe795e44175362d22f4bba036312/$', FacebookWebhookView.as_view(), name='webhook'),]