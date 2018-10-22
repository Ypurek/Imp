from django.contrib import admin
from django.urls import path, include
from ui.views import auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ui.urls'), name='ui'),
    path('ws', include('ws.urls'), name='ws'),

    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    # path('signup/', auth_views.signup, name='signup'),
    path('logout/', auth_views.login_view, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),

]
