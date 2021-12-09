from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippet'),
    path('snippets/list/my', views.my_snippets_page, name='my_list_snippet'),
    path('snippets/<int:id>', views.get_snippet, name='get_snippet'),
    path('snippets/edit/<int:id>', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>', views.delete_snippet, name='delete_snippet'),
    path('auth/login', views.login_page, name='login'),
    path('auth/logout', views.logout, name='logout'),
    path('auth/register', views.register, name="register"),
    path('comment/add', views.comment_add, name="comment_add"),
    path('comment/edit/<int:id>', views.comment_edit, name="comment_edit"),
    path('comment/delete/<int:id>', views.comment_delete, name="comment_delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
