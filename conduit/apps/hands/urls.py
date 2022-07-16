
from django.urls import path
from . import views

urlpatterns = [
    # TODO: 正規表現で予めフォーマットを指定しておきたい
    # path(r'^hands/(?P<current_tiles_by_one_line_string>[1-9mpsz]+)/shanten_advanceable_tiles/?$', views.shanten_advanceable_tiles),
    path('hands/<str:one_line_string_tiles>/shanten_advanceable_tiles', views.shanten_advanceable_tiles),
]
