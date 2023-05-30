from django.urls import path, include
from rest_framework import routers

from . import views_api

#ruter do widokow API
api_router = routers.DefaultRouter()

api_router.register('users', views_api.UserViewSet)
api_router.register('question', views_api.QuestionViewSet)
api_router.register('quiz', views_api.QuizViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('', include(api_router.urls)),
    path('', include(api_router.urls))
]
