from django.contrib import admin
from django.urls import path

#now import the views.py file into this code
from . import views
from .views import MyView
urlpatterns = [
  path('admin/', admin.site.urls),
  # path('', views.home_view),
  # path('', views.formset_view),
  # path('', views.model_view),
  # path('', views.geeks_view),
  # path('', views.my_view),
  # path('', views.list_view),
  # path('', views.create_view),
  # path('<id>/', views.detail_view),
  # path('<id>/update', views.update_view),
  # path('<id>/delete', views.delete_view),
  # path('about/', MyView.as_view()),
  # path('', views.GeeksCreate.as_view()),
  path('', views.GeeksList.as_view()),
  path('<pk>/', views.GeeksDetailView.as_view()),
  path('<pk>/update', views.GeeksUpdateView.as_view()),
  path('<pk>/delete/', views.GeeksDeleteView.as_view()),
  # path('', views.GeeksFormView.as_view()),
]