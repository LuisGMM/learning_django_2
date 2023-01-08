from django.urls import path

from learning_django_2.store import views



# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail)
]
