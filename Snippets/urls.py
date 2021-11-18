from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippet'),
    path('snippets/<int:id>', views.get_snippet, name='get_snippet'),
    path('snippets/edit/<int:id>', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>', views.delete_snippet, name='delete_snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

