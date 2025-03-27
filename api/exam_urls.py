# api/exam_urls.py

from django.urls import path
from .exam_views import ChatView  # Ensure this points to the correct ChatView

urlpatterns = [
    path("chat/", ChatView.as_view(), name="chat"),  # This will handle /api/exam/chat/
]