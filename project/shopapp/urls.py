from unicodedata import name
from django.urls import path
from . import views
app_name='shopapp'


urlpatterns = [
    path('', views.allProduct,name='allProduct'),
    path('<slug:c_slug>/', views.allProduct,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail,name='productdetail')

]