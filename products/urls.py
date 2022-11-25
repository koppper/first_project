from django.urls import path, re_path
from .views import index, second_list, hello_sky_learn

urlpatterns = [
    path('sky_learn/', hello_sky_learn)
]
