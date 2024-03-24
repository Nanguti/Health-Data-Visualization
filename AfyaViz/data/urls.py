from django.urls import path
from . import views

urlpatterns = [
  # Data Source Endpoints
  path('data-sources/', views.DataSourceList.as_view(), name='data-source-list'),
  path('data-sources/<int:pk>/', views.DataSourceDetail.as_view(), name='data-source-detail'),

  # Data Set Endpoints
  path('datasets/', views.DataSetList.as_view(), name='dataset-list'),
  path('datasets/<int:pk>/', views.DataSetDetail.as_view(), name='dataset-detail'),

  # Variable Endpoints
  path('datasets/<int:pk>/variables/', views.VariableListByDataset.as_view(), name='variable-list-by-dataset'),

  # Data Point Endpoints
  path('datapoints/<int:datapoint_id>/', views.DataListView.as_view()), 
  path('datapoints/dataset/<int:dataset_id>/', views.DataListView.as_view()),
  path('datasets/<int:dataset_pk>/variables/<int:variable_pk>/data-points/', views.DataPointListByDatasetVariable.as_view(), name='data-point-list-by-dataset-variable'),

  path('datapoints/', views.DataListView.as_view(), name='data-points')
]
