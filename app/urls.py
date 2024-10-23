from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.Index, name='index'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('join_us/', views.Join_us, name='join_us'),
    path('profile/', views.Profile, name='profile'),
    path('save_application/', views.Save_Application, name='save_application'),
    path('news_events/', views.News_Events, name='news_events'),
    path('news_events/<int:id>/', views.News_or_Event, name='news_or_event'),
    path('library/', views.Library, name='library'),
    path('resource/', views.Resource, name='resource'),
    path('members/', views.Members, name='members'),
    path('governance/', views.Governance, name='governance'),
    path('management/', views.Management, name='management'),
    path('members/profile/<int:id>/', views.Profile, name='profile'),
    path('applications/', views.Applications, name='applications'),
    path('applications/ChangeStatus/', views.ChangeStatus, name='ChangeStatus'),
    path('library/<int:document_id>/', views.serve_pdf, name='serve_pdf'),
]
