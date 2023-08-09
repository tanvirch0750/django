from book.views import delete_book, edit_book, home, show_books, store_book
from django.urls import path

from . import views

urlpatterns = [
    # path('', home, name="home"),
    # path('show_books/', show_books, name="show_books"),
    # path('store_book/', store_book, name="store_book"),
    # path('edit_book/<int:id>', edit_book, name="edit_book"),
    # path('delete_book/<int:id>', delete_book, name="delete_book")
    # path('', views.TemplateView.as_view(template_name='home.html')), -> we can directly render template without views like this
    # path('<int:roll>/', views.HomeTemplateView.as_view(), {'author': 'karim'}, name='home'),
    path('', views.HomeTemplateView.as_view(), {'author': 'karim'}, name='home'),
    path('store_book/', views.BookFormView.as_view(), name="store_book"),
    path('show_books/', views.BookListView.as_view(), name="show_books"),
    path('detail_book/<int:id>', views.BookDetailsView.as_view(), name="detail_book"),
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>', views.BookDeleteView.as_view(), name="delete_book")
]