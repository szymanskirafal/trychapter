from django.urls import path
from django.views import generic

app_name = 'books'
urlpatterns = [
    path(
        'add-book/',
        generic.TemplateView.as_view(template_name="pages/add-book.html"),
        name="add_book",
    ),

]
