"""ProjectSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from login import views as views_login
from admin_resign import views as views_resign
from student_project import views as views_studentproject
from teacher_project import views as views_teacherproject

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'about/$', views_login.about),
    url(r'login/$',views_login.index),
    url(r'login/register/$',views_resign.index),
    url(r'login/logout/$',views_login.logout),
    url(r'student/project/list/$',views_studentproject.index),
    url(r'student/project/list/(\d+)/$',views_studentproject.showproject),
    url(r'teacher/project/list/$',views_teacherproject.index),
    url(r'teacher/project/list/(\d+)/$',views_teacherproject.showproject),
    url(r'teacher/project/list/(\d+)/(\w+)/$', views_teacherproject.show_project_apply),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
