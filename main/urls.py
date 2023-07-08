from django.urls import path
from . views import* 

urlpatterns = [
    path('', home, name="index"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('vote/', page_vote, name="vote"),
    path('logout/', logout_view, name='logout'),
    path('results/',results, name='results'),
   
]