from django.urls import path
from product.views import get_all_product, get_one_product, create_data, edit_data, update_data, delete_data
urlpatterns = [
    path('read/', get_all_product, name='index'),
    path('read/<int:id>', get_one_product),
    path('save/', create_data),
    path('edit/<int:id>', edit_data),
    path('update/<int:id>', update_data),
    path('delete/<int:id>', delete_data),
]
