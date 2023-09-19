from django.urls import path

from modules_app.views.functions_table_view import get_functions_table

urlpatterns = [
    path('', get_functions_table, name='functions_table'),
]
