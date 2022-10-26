from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, SearchList, CreatePost, DeletePost, EditPost, CategoryListView, subscribe

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search', SearchList.as_view(), name='post_search'),
   path('create', CreatePost.as_view(), name='post_create'),
   path('<int:pk>/edit', EditPost.as_view(), name='post_edit'),
   path('<int:pk>/delete', DeletePost.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]