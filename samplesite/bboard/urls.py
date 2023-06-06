from django.urls import path

from .views import index, rubric_bbs

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
]