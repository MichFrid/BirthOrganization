from django.urls import path, include
from .views import homepage


urlpatterns = [
    path('', homepage),
]
# urlpatterns = [
#     path("", views.serve_home),
#     path('home', views.serve_home),]

# urlpatterns = [
#     path("today", views.today_date),
#     #path("coins", views.today_coins),
#     path("", views.serve_home),
#     path("home-html", views.serve_html),
#     path("show-params", views.ex2),
#     path('hello', views.hello_view, name='hello'),
#     path('bye', views.bye_view, name='bye'),
# ]
