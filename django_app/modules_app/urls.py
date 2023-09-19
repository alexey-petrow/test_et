from django.urls import path

from modules_app.views import functions_table_views, json_handle_views

urlpatterns = [
    path('', functions_table_views.get_functions_table, name='functions_table'),
    path('json/', json_handle_views.JsonHandlerAPIView.as_view(), name='json_api'),
]
