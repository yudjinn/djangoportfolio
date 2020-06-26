from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from resume import views as resume_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('resume/', resume_views.resume, name='resume'),
    path('', include('landing.urls')),
]
