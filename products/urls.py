from django.urls import path
from products.views import (
	product_detail_view,
	product_create_view,
	dynamic_lookup_view,
	product_update_view,
	product_delete_view,
	product_list_view
	)
app_name = 'products'
urlpatterns = [
    path('', product_list_view),
	path('create/', product_create_view),
    #path('product/', product_detail_view),
	path('<int:my_id>/', dynamic_lookup_view, name= 'product-detail'),
	path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
	path('<int:my_id>/update/', product_update_view, name='product-update'), 
	
	
]