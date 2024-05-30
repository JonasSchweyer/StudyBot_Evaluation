from django.urls import path

from api import chatbot

urlpatterns = [
    path('messages/v1/', chatbot.chat1_english),
    path('messages/v2/', chatbot.chat2_german),
    path('messages/v3/', chatbot.chat3_mixed),
]