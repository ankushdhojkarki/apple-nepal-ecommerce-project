from django.urls import path
from .views import categories_view, category_detail_view

urlpatterns = [
    path('', categories_view, name = 'categories'),
    path('<int:category_id>/', category_detail_view, name='category_detail'),

]    