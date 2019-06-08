from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'api/foss/(?P<fid>[0-9]+)/tutorials/', views.TutorialDetailList.as_view()), 
  url(r'api/foss/', views.ContributorRoleList.as_view()), 
  url(r'api/tutorial/(?P<tid>[0-9]+)/script/create/$', views.ScriptCreateAPIView.as_view()),
  url(r'', views.index, name='home'),
]
