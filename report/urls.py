from django.urls import path

from report import views


urlpatterns = [
    # acs.core
    path('reports',
         views.ReportsListView.as_view(),
         name='reports')
    ]
