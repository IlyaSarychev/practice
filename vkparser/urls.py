from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('request-result/', views.SearchResultView.as_view(), name='request_result'),
    path('post-items/', views.post_items_view, name='post_items'),
    path('database/', views.DataListView.as_view(), name='database'),
    path('delete/<str:collection>/<int:id>/', views.delete_item_view, name='delete'),
    path('extract-prnu/<str:collection>/<int:id>/', views.PRNUExtractionView.as_view(), name='extract_prnu'),
]