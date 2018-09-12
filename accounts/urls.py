from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [

    #path('accounts/',views.post_list1),
    path('signup/',views.signup, name='signup'),
    path('login/',auth_views.login, name='login', kwargs={'template_name':'accounts/login_form.html'}),
    path('logout/',auth_views.logout, name='logout', kwargs={'next_page':settings.LOGIN_URL}),
    path('profile/',views.profile, name='profile'),

]





