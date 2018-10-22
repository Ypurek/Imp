from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ui.urls'), name='ui'),
    path('ws', include('ws.urls'), name='ws'),

    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # path('signup/', auth_views.signup, name='signup'),
    path('logout/', auth_views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),

]
