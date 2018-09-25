from django.urls import path
from . import views

app_name = 'store'

# add urls/routes here
# the parameters of path are path(directory, functions inside views.py that will throw and recieve, url name/label)
urlpatterns = [
    # /[app name]/id/url
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
]
