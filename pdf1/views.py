from .models import Book
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    paginate_by = 3

class AddBookView(CreateView):
    model = Book
    form_class = BookForm

    success_url = reverse_lazy('home')
    template_name = 'addbook.html'

